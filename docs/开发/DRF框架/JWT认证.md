## <font style="color:rgb(39, 38, 43);">什么是Json Web Token?</font>
<font style="color:rgb(92, 89, 98);">JSON Web Token（JWT）是一种开放标准，它定义了一种紧凑且自包含的方式，用于各方之间安全地将信息以JSON对象传输。由于此信息是经过数字签名的，因此可以被验证和信任。JWT用于为应用程序创建访问token，通常适用于API身份验证和服务器到服务器的授权。那么如何理解紧凑和自包含这两个词的含义呢?</font>

+ **<font style="color:rgb(92, 89, 98);">紧凑</font>**<font style="color:rgb(92, 89, 98);">：就是说这个数据量比较少，可以通过url参数，http请求提交的数据以及http header多种方式来传递。</font>
+ **<font style="color:rgb(92, 89, 98);">自包含</font>**<font style="color:rgb(92, 89, 98);">：这个字符串可以包含很多信息，比如用户id，用户名，订单号id等，如果其他人拿到该信息，就可以拿到关键业务信息。</font>
+ ![](../../images/1727942358141-c38e3e13-13c2-4354-a0d5-bc000c46ae40.png)

<font style="color:rgb(92, 89, 98);">那么JWT认证是如何工作的呢? 首先客户端提交用户登录信息验证身份通过后，服务器生成一个用于证明用户身份的令牌(token)，也就是一个加密后的长字符串，并将其发送给客户端。在后续请求中，客户端以各种方式(比如通过url参数或者请求头)将这个令牌发送回服务器，服务器就知道请求来自哪个特定身份的用户了。</font>

<font style="color:rgb(92, 89, 98);">SON Web Token由三部分组成，这些部分由点（.）分隔，分别是header(头部)，payload(有效负载)和signature(签名)。</font>

+ **<font style="color:rgb(92, 89, 98);">header(头部)</font>**<font style="color:rgb(92, 89, 98);">: 识别以何种算法来生成签名；</font>
+ **<font style="color:rgb(92, 89, 98);">pyload(有效负载)</font>**<font style="color:rgb(92, 89, 98);">: 用来存放实际需要传递的数据；</font>
+ **<font style="color:rgb(92, 89, 98);">signature(签名):</font>**<font style="color:rgb(92, 89, 98);"> </font><font style="color:rgb(92, 89, 98);">安全验证token有效性，防止数据被篡改。</font>

<font style="color:rgb(92, 89, 98);">通过http传输的数据实际上是加密后的JWT，它是由两个点分割的base64-URL长字符串组成，解密后我们可以得到header, payload和signature三部分。我们可以简单的使用 https://jwt.io/ 官网来生成或解析一个JWT，如下所示：</font>![](../../images/1727942352852-d4c0bf0a-a11f-4022-a1ad-50e17b468338.png)

<font style="color:rgb(92, 89, 98);">接下来我们将使用django-rest-framework-simplejwt这个第三方软件包进行JWT身份验证。</font>

## <font style="color:rgb(39, 38, 43);">DRF中如何使用JWT认证</font>
### <font style="color:rgb(39, 38, 43);">安装</font>
<font style="color:rgb(92, 89, 98);">django-rest-framework-simplejwt为Django REST Framework提供了JSON Web Token认证后端。它提供了一组保守的默认功能来涵盖了JWT的最常见用例，而且非常容易扩展。</font>

**<font style="color:rgb(92, 89, 98);">首先</font>**<font style="color:rgb(92, 89, 98);">，我们要使用pip安装它。</font>

```python
poetry add djangorestframework-simplejwt
```

**<font style="color:rgb(92, 89, 98);">其次</font>**<font style="color:rgb(92, 89, 98);">，我们需要告诉DRF我们使用jwt认证作为后台认证方案。修改</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">apiproject/settings.py</font>`<font style="color:rgb(92, 89, 98);">：</font>

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}
```

**<font style="color:rgb(92, 89, 98);">最后</font>**<font style="color:rgb(92, 89, 98);">，我们需要提供用户可以获取和刷新token的urls地址，这两个urls分别对应</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">TokenObtainPairView</font>`<font style="color:rgb(92, 89, 98);">和</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">TokenRefreshView</font>`<font style="color:rgb(92, 89, 98);">两个视图。</font>

```python
from django.contrib import admin
from django.urls import path, include
from reviews.views import ProductViewSet, ImageViewSet
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
TokenObtainPairView,
TokenRefreshView,
)

router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='Product')
router.register(r'image', ImageViewSet, basename='Image')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### <font style="color:rgb(39, 38, 43);">测试</font>
<font style="color:rgb(92, 89, 98);">现在我们可以开始使用postman测试了。通过POST方法发送登录请求到/token/, 请求数据包括username和password。如果登录成功，你将得到两个长字符串，一个是access token(访问令牌)，还有一个是refresh token(刷新令牌)，如下所示：</font>

```python
{
	"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyODAyOTMzNSwiaWF0IjoxNzI3OTQyOTM1LCJqdGkiOiJhZmNlNDA3ZmMyZTA0YjYwYTdhMzU4YTU2ZDZlODI0MyIsInVzZXJfaWQiOjF9.mfyww_kQjQVR8XDcZcwiuAOho4Jw5DockDqO7Pnnbvg",
	"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI3OTQzMjM1LCJpYXQiOjE3Mjc5NDI5MzUsImp0aSI6IjUwZTBkYTRkNjg2MjRkN2Y5ZTJlYjg4MzE3YzE5OTc2IiwidXNlcl9pZCI6MX0.GE0kyRwaWnG-0pfncePaSysXfzJ2xLs2k3lBDU6n1Fg"
}
```

<font style="color:rgb(92, 89, 98);"></font>

<font style="color:rgb(92, 89, 98);"></font>

<font style="color:rgb(92, 89, 98);">假如你有一个受保护的视图(比如这里的/image/)，权限(permission_classes)是</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">IsAuthenticated</font>`<font style="color:rgb(92, 89, 98);">，只有验证用户才可访问。访问这个保护视图时你只需要在请求头的Authorization选项里输入你刚才获取的access token即可，如下所示：</font>

```python
{
	"detail": "身份认证信息未提供。"
}
```

```python
Authorization
Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI3OTQzMjM1LCJpYXQiOjE3Mjc5NDI5MzUsImp0aSI6IjUwZTBkYTRkNjg2MjRkN2Y5ZTJlYjg4MzE3YzE5OTc2IiwidXNlcl9pZCI6MX0.GE0kyRwaWnG-0pfncePaSysXfzJ2xLs2k3lBDU6n1Fg
```

```python
{
	"count": 6,
	"next": null,
	"previous": null,
	"results": [
		{
			"id": 7,
			"title": "django",
			"author": {
				"id": 1,
				"username": "admin",
				"articles": [
					"http://127.0.0.1:8000/blog/v1/articles/7/",
					"http://127.0.0.1:8000/blog/v1/articles/6/",
					"http://127.0.0.1:8000/blog/v1/articles/5/",
					"http://127.0.0.1:8000/blog/v1/articles/4/",
					"http://127.0.0.1:8000/blog/v1/articles/2/",
					"http://127.0.0.1:8000/blog/v1/articles/1/"
				]
			},
			"full_status": "Draft",
			"cn_status": "草稿",
			"create_date": "2024-10-03 14:12:39",
			"body": "django",
			"status": "d"
		},
		{
			"id": 6,
			"title": "sss",
			"author": {
				"id": 1,
				"username": "admin",
				"articles": [
					"http://127.0.0.1:8000/blog/v1/articles/7/",
					"http://127.0.0.1:8000/blog/v1/articles/6/",
					"http://127.0.0.1:8000/blog/v1/articles/5/",
					"http://127.0.0.1:8000/blog/v1/articles/4/",
					"http://127.0.0.1:8000/blog/v1/articles/2/",
					"http://127.0.0.1:8000/blog/v1/articles/1/"
				]
			},
			"full_status": "Published",
			"cn_status": "已发表",
			"create_date": "2024-10-03 13:08:17",
			"body": "sss",
			"status": "p"
		},
		{
			"id": 5,
			"title": "111",
			"author": {
				"id": 1,
				"username": "admin",
				"articles": [
					"http://127.0.0.1:8000/blog/v1/articles/7/",
					"http://127.0.0.1:8000/blog/v1/articles/6/",
					"http://127.0.0.1:8000/blog/v1/articles/5/",
					"http://127.0.0.1:8000/blog/v1/articles/4/",
					"http://127.0.0.1:8000/blog/v1/articles/2/",
					"http://127.0.0.1:8000/blog/v1/articles/1/"
				]
			},
			"full_status": "Draft",
			"cn_status": "草稿",
			"create_date": "2024-10-02 23:59:21",
			"body": "nihao",
			"status": "d"
		},
		{
			"id": 4,
			"title": "sda",
			"author": {
				"id": 1,
				"username": "admin",
				"articles": [
					"http://127.0.0.1:8000/blog/v1/articles/7/",
					"http://127.0.0.1:8000/blog/v1/articles/6/",
					"http://127.0.0.1:8000/blog/v1/articles/5/",
					"http://127.0.0.1:8000/blog/v1/articles/4/",
					"http://127.0.0.1:8000/blog/v1/articles/2/",
					"http://127.0.0.1:8000/blog/v1/articles/1/"
				]
			},
			"full_status": null,
			"cn_status": "",
			"create_date": "2024-10-02 23:33:03",
			"body": "sdasdasd",
			"status": null
		},
		{
			"id": 2,
			"title": "Updated Title",
			"author": {
				"id": 1,
				"username": "admin",
				"articles": [
					"http://127.0.0.1:8000/blog/v1/articles/7/",
					"http://127.0.0.1:8000/blog/v1/articles/6/",
					"http://127.0.0.1:8000/blog/v1/articles/5/",
					"http://127.0.0.1:8000/blog/v1/articles/4/",
					"http://127.0.0.1:8000/blog/v1/articles/2/",
					"http://127.0.0.1:8000/blog/v1/articles/1/"
				]
			},
			"full_status": "Draft",
			"cn_status": "草稿",
			"create_date": "2024-10-02 23:25:14",
			"body": "Updated content.",
			"status": "d"
		},
		{
			"id": 1,
			"title": "Updated Title",
			"author": {
				"id": 1,
				"username": "admin",
				"articles": [
					"http://127.0.0.1:8000/blog/v1/articles/7/",
					"http://127.0.0.1:8000/blog/v1/articles/6/",
					"http://127.0.0.1:8000/blog/v1/articles/5/",
					"http://127.0.0.1:8000/blog/v1/articles/4/",
					"http://127.0.0.1:8000/blog/v1/articles/2/",
					"http://127.0.0.1:8000/blog/v1/articles/1/"
				]
			},
			"full_status": "Published",
			"cn_status": "已发表",
			"create_date": "2024-10-02 23:18:06",
			"body": "Updated content.",
			"status": "p"
		}
	]
}
```

<font style="color:rgb(92, 89, 98);">不过这个access token默认只有5分钟有效。5分钟过后，当你再次访问保护视图时，你将得到如下token已失效或过期的提示：</font>

```python
{
	"detail": "Given token not valid for any token type",
	"code": "token_not_valid",
	"messages": [
		{
			"token_class": "AccessToken",
			"token_type": "access",
			"message": "Token is invalid or expired"
		}
	]
}
```

<font style="color:rgb(92, 89, 98);"></font>

<font style="color:rgb(92, 89, 98);">去获取新的access token，你需要使用之前获得的refresh token。你将这个refresh token放到请求的正文(body)(form-data和raw都可以)里，发送POST请求到</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">/token/refresh/</font>`<font style="color:rgb(92, 89, 98);">即可获得刷新后的access token(访问令牌), 如下所示：</font>

```python
{
	"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI3OTQzODE0LCJpYXQiOjE3Mjc5NDMzMTEsImp0aSI6IjBmNTc1NjU2ZGRkZTQwOWNiNWMxZWNhZjE2MTc2MzFiIiwidXNlcl9pZCI6MX0.9Gm6z1zqwdALwKFHUqSCKYx77ImeQZnzsop9Hd8RLoI"
}
```

<font style="color:rgb(92, 89, 98);">那么问题来了，Simple JWT中的access token默认有效期是5分钟，那么refresh token默认有效期是多长呢? 答案是24小时。</font>



## <font style="color:rgb(39, 38, 43);">Simple JWT的默认设置</font>
<font style="color:rgb(92, 89, 98);">Simple JWT的默认设置如下所示：</font>

```python
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
}
```

<font style="color:rgb(92, 89, 98);">如果要覆盖Simple JWT的默认设置，可以修改</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">settings.py</font>`<font style="color:rgb(92, 89, 98);">, 如下所示。下例将refresh token的有效期改为了15天。</font>

```python
from datetime import timedelta


SIMPLE_JWT = {
    'REFRESH_TOKEN_LIFETIME': timedelta(days=15),
    'ROTATE_REFRESH_TOKENS': True,
}
```

## <font style="color:rgb(39, 38, 43);">自定义令牌(token)</font>
<font style="color:rgb(92, 89, 98);">如果你对Simple JWT返回的access token进行解码，你会发现这个token的payload数据部分包括token类型，token失效时间，jti(一个类似随机字符串）和user_id。如果你希望在payload部分提供更多信息，比如用户的username，这时你就要自定义令牌(token)了。</font>

![](../../images/1727942516661-a0648e33-6bc6-4d75-a3d4-9f3ab397882f.png)



**<font style="color:rgb(92, 89, 98);">首先</font>**<font style="color:rgb(92, 89, 98);">，编写你的</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">myapp/seralizers.py</font>`<font style="color:rgb(92, 89, 98);">，添加如下代码。该序列化器继承了</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">TokenObtainPairSerializer</font>`<font style="color:rgb(92, 89, 98);">类。</font>

```python
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # 添加额外信息
        token['username'] = user.username
        return token
```

**<font style="color:rgb(92, 89, 98);">其次</font>**<font style="color:rgb(92, 89, 98);">，不使用Simple JWT提供的默认视图，使用自定义视图。修改</font><font style="color:rgb(92, 89, 98);"> </font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">myapp/views.py</font>`<font style="color:rgb(92, 89, 98);">, 添加如下代码：</font>

```python
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from .serializers import MyTokenObtainPairSerializer

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
```

**<font style="color:rgb(92, 89, 98);">最后</font>**<font style="color:rgb(92, 89, 98);">，修改</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">apiproject/urls.py</font>`<font style="color:rgb(92, 89, 98);">, 添加如下代码，将/token/指向新的自定义的视图。注意：本例中的app名为reviews，所以是从reviews.views导入的</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">MyObtainTokenPairView</font>`<font style="color:rgb(92, 89, 98);">。</font>

```python
from django.contrib import admin
from django.urls import path, include
from reviews.views import ProductViewSet, ImageViewSet, MyObtainTokenPairView
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='Product')
router.register(r'image', ImageViewSet, basename='Image')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

<font style="color:rgb(92, 89, 98);">重新发送POST请求到/token/，你将获得新的access token和refresh token，如下所示：</font>

<font style="color:rgb(92, 89, 98);"></font>

<font style="color:rgb(92, 89, 98);"></font>

<font style="color:rgb(92, 89, 98);"></font>

<font style="color:rgb(92, 89, 98);">对重新获取的access token进行解码，你将看到payload部分多了username的内容，是不是很酷? 在实际API开发过程中，通过Json Web Token传递更多数据非常有用。</font>

<font style="color:rgb(92, 89, 98);">  
</font><font style="color:rgb(92, 89, 98);"> </font>

## <font style="color:rgb(39, 38, 43);">自定义认证后台(Backend)</font>
<font style="color:rgb(92, 89, 98);">上面的演示案例是通过用户名和密码登录的，如果我们希望后台同时支持邮箱/密码，手机/密码组合登录怎么办? 这时我们还需要自定义认证后台(Backend)。</font>

**<font style="color:rgb(92, 89, 98);">首先</font>**<font style="color:rgb(92, 89, 98);">，修改</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">users/views.py</font>`<font style="color:rgb(92, 89, 98);">, 添加如下代码：</font>

```python
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.contrib.auth import get_user_model

User = get_user_model()

class MyCustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username) )
            if user.check_password(password):
                return user
        except Exception as e:
            return None
```

**<font style="color:rgb(92, 89, 98);">其次</font>**<font style="color:rgb(92, 89, 98);">，修改</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">settings.py</font>`<font style="color:rgb(92, 89, 98);">, 把你自定义的验证方式添加到AUTHENTICATION_BACKENDS里去。</font>

```python
AUTHENTICATION_BACKENDS = (
    'users.views.MyCustomBackend',
)
```

<font style="color:rgb(92, 89, 98);">修改好后，你使用postman发送邮箱/密码组合到/token/，将同样可以获得access token和refresh token。是不是又学到了一招?</font>

## <font style="color:rgb(39, 38, 43);">小结</font>
<font style="color:rgb(92, 89, 98);">本文讲解与演示的内容非常多，介绍了什么是JWT及其工作原理，演示了如何使用Simple JWT这个第三方安装包，如何自定义令牌(token)和认证后台(backend)。</font>

