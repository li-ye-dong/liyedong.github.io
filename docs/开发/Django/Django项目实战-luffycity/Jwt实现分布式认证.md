```python
pip install djangorestframework-simplejwt
```

```python
# drf配置
REST_FRAMEWORK = {
    # 自定义异常处理
    'EXCEPTION_HANDLER': 'luffycityapi.utils.exceptions.exception_handler',
    # 自定义认证
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',  # jwt认证
        'rest_framework.authentication.SessionAuthentication',  # session认证
        'rest_framework.authentication.BasicAuthentication',
    ),
}
import datetime

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(minutes=5),  # 访问令牌（Access Token）的有效期，设置为5分钟
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=1),    # 刷新令牌（Refresh Token）的有效期，设置为1天
    'ROTATE_REFRESH_TOKENS': False,                          # 是否在刷新令牌时生成新的刷新令牌，False 表示不生成新令牌
    'BLACKLIST_AFTER_ROTATION': True,                        # 在刷新令牌旋转后是否将旧令牌加入黑名单，True 表示加入黑名单

    'ALGORITHM': 'HS256',                                    # JWT 签名使用的加密算法，HS256 是基于 HMAC-SHA256 的对称加密
    'SIGNING_KEY': SECRET_KEY,                               # 用于签名的密钥，这里使用 Django 的 SECRET_KEY
    'VERIFYING_KEY': None,                                   # 用于验证签名的密钥，None 表示使用 SIGNING_KEY（对称加密时适用）
    'AUDIENCE': None,                                        # JWT 的接收者（audience），None 表示不指定
    'ISSUER': None,                                          # JWT 的发行者（issuer），None 表示不指定

    'AUTH_HEADER_TYPES': ('Bearer',),                        # 认证请求头中支持的类型，设置为 Bearer（常见的 JWT 认证方式）
    'USER_ID_FIELD': 'id',                                   # 用户模型中表示用户 ID 的字段名，默认为 id
    'USER_ID_CLAIM': 'user_id',                              # JWT 中存储用户 ID 的声明（claim）名称，设置为 user_id

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),  # 支持的令牌类，这里只使用 AccessToken
    'TOKEN_TYPE_CLAIM': 'token_type',                        # JWT 中表示令牌类型的声明名称，设置为 token_type

    'JTI_CLAIM': 'jti',                                      # JWT 中唯一标识符（JWT ID）的声明名称，设置为 jti

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',        # 滑动令牌刷新到期时间的声明名称，设置为 refresh_exp
    'SLIDING_TOKEN_LIFETIME': datetime.timedelta(minutes=5), # 滑动令牌（Sliding Token）的有效期，设置为5分钟（类似于 Access Token）
    'SLIDING_TOKEN_REFRESH_LIFETIME': datetime.timedelta(days=1),  # 滑动令牌的刷新令牌有效期，设置为1天
    "TOKEN_OBTAIN_SERIALIZER": "users.serializers.MyTokenObtainPairSerializer",
}
AUTHENTICATION_BACKENDS = (
    'users.views.MyCustomBackend',
    'django.contrib.auth.backends.ModelBackend',  # 保留默认的
)

```

users.views.MyCustomBackend,自定义认证后台，允许使用手机号码和用户名和邮箱登录，需要再修改配置文件，启用如下自定义后台验证

```python
import random

from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django_redis import get_redis_connection
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .tasks import send_email


class MyCustomBackend(ModelBackend):
    """
    自定义认证后台，允许使用手机号码和用户名和邮箱登录，需要再修改配置文件，启用如下自定义后台验证
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        user = User.objects.get(Q(username=username) | Q(email=username) | Q(mobile=username))
        if user.check_password(password):
            return user
```



serializers.py，自定义返回的token字段或者自定义token内容

```python
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    自定义token序列化器
    1.继承TokenObtainPairSerializer
    2.更新配置文件，指定自定义序列化器
    """

    @classmethod
    def get_token(cls, user):
        """添加自定义token生成字段"""
        token = super().get_token(user)

        # 添加额外信息
        if hasattr(user, 'avatar'):
            token['avatar'] = user.avatar.url if user.avatar else ""
        if hasattr(user, 'nickname'):
            token['nickname'] = user.nickname
        if hasattr(user, 'money'):
            token['money'] = float(user.money)
        if hasattr(user, 'credit'):
            token['credit'] = user.credit

        return token

    # 自定义登录成功的返回字段
    def validate(self, attrs):
        # 继承父类，然后才可以调用self.user获取到，不然无法传递self变量
        data = super().validate(attrs)
        access_token = data['access']
        redis = get_redis_connection("cart")
        cart_total = redis.hlen(f"cart_{self.user.id}")

        # 自定义字段名并添加额外信息
        custom_response = {
            'cart_total': cart_total,
            "token": access_token,
        }
        return custom_response


class MyTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        # 直接继承父类，不动
        return super().get_token(user)
```



配置路由urls.py

```python
from django.urls import path, re_path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    #path("login/", MyTokenView.as_view(), name="token_obtain_pair"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("login/verify", TokenVerifyView.as_view(), name="token_verify"),
]
# obtain_jwt_token实际上就是 rest_framework_jwt.views.ObtainJSONWebToken.as_view()

# 登录视图，获取access_token
# obtain_jwt_token = ObtainJSONWebToken.as_view()
# 刷新token视图，依靠旧的access_token生成新的access_token
# refresh_jwt_token = RefreshJSONWebToken.as_view()
# 验证现有的access_token是否有效
# verify_jwt_token = VerifyJSONWebToken.as_view()

```



