# <font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">入门</font>
## <font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">要求</font>
+ <font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">Python（3.8，3.9，3.10，3.11）</font>
+ <font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">Django（3.2，4.0，4.1，4.2）</font>
+ <font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">Django REST框架（3.10，3.11，3.12，3.13，3.14）</font>

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">这些是官方支持的python和包版本。 其他版本可能会工作。 您可以自由修改tox配置并看看有什么可能。</font>

## <font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">安装</font>
<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">简单的JWT可以通过pip安装：</font>

```python
pip install djangorestframework-simplejwt
```

## <font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">加密验证（可选）</font>
<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">如果您计划使用某些数字签名算法（即RSA和ECDSA;访问PyJWT了解其他算法）对令牌进行编码或解码，则需要安装</font>[<font style="color:rgb(41, 128, 185);background-color:rgb(252, 252, 252);">加密</font>](https://cryptography.io/)<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">库。这可以显式安装，也可以作为</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">djangorestframework-simplejwt</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">需求中的必需附加项安装：</font>

```python
pip install djangorestframework-simplejwt[crypto]
```

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">在使用</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">djangorestframework-simplejwt[crypto]</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">的项目中，建议在需求文件中使用</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">Simple</font><font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);"> </font><font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">JWT</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">格式，因为单独的</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">cryptography</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">需求行可能会被误认为未使用的需求并被删除。</font>

## <font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">项目配置</font>
<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">然后，您的django项目必须配置为使用该库。 在</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">settings.py</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">中，将</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">rest_framework_simplejwt.authentication.JWTAuthentication</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">添加到身份验证类列表中：</font>

```python
REST_FRAMEWORK = {
    ...
    'DEFAULT_AUTHENTICATION_CLASSES': (
    ...
    'rest_framework_simplejwt.authentication.JWTAuthentication',
)
...
}
```

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">另外，在你的根</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">urls.py</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">文件（或任何其他url配置）中，包括Simple JWT的</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">TokenObtainPairView</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">和</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">TokenRefreshView</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">视图的路由：</font>

```python
from rest_framework_simplejwt.views import (
TokenObtainPairView,
TokenRefreshView,
)

urlpatterns = [
    ...
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ...
]
```

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">如果您希望允许API用户在不访问您的签名密钥的情况下验证HMAC签名的令牌，您还可以包含Simple JWT的</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">TokenVerifyView</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">路由：</font>

```python
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    ...
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    ...
]
```

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">如果您希望使用本地化/翻译，只需将</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">rest_framework_simplejwt</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">添加到</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">INSTALLED_APPS</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">。</font>

```python
INSTALLED_APPS = [
    ...
    'rest_framework_simplejwt',
...
]
```

## <font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">使用</font>
<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">要验证Simple JWT是否正常工作，您可以使用curl发出几个测试请求：</font>

```python
curl \
-X POST \
-H "Content-Type: application/json" \
-d '{"username": "davidattenborough", "password": "boatymcboatface"}' \
http://localhost:8000/api/token/

...
{
    "access":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiY29sZF9zdHVmZiI6IuKYgyIsImV4cCI6MTIzNDU2LCJqdGkiOiJmZDJmOWQ1ZTFhN2M0MmU4OTQ5MzVlMzYyYmNhOGJjYSJ9.NHlztMGER7UADHZJlxNG0WSi22a2KaYSfd1S-AuT7lU",
    "refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImNvbGRfc3R1ZmYiOiLimIMiLCJleHAiOjIzNDU2NywianRpIjoiZGUxMmY0ZTY3MDY4NDI3ODg5ZjE1YWMyNzcwZGEwNTEifQ.aEoAYkSJjoWH1boshQAaTkf8G3yn0kapko6HFRt7Rh4"
}
```

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">您可以使用返回的访问令牌来证明受保护视图的身份验证：</font>

```python
curl \
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiY29sZF9zdHVmZiI6IuKYgyIsImV4cCI6MTIzNDU2LCJqdGkiOiJmZDJmOWQ1ZTFhN2M0MmU4OTQ5MzVlMzYyYmNhOGJjYSJ9.NHlztMGER7UADHZJlxNG0WSi22a2KaYSfd1S-AuT7lU" \
http://localhost:8000/api/some-protected-view/
```

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">当此短期访问令牌过期时，您可以使用长期刷新令牌来获取另一个访问令牌：</font>

```python
curl \
-X POST \
-H "Content-Type: application/json" \
-d '{"refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImNvbGRfc3R1ZmYiOiLimIMiLCJleHAiOjIzNDU2NywianRpIjoiZGUxMmY0ZTY3MDY4NDI3ODg5ZjE1YWMyNzcwZGEwNTEifQ.aEoAYkSJjoWH1boshQAaTkf8G3yn0kapko6HFRt7Rh4"}' \
http://localhost:8000/api/token/refresh/

...
{"access":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiY29sZF9zdHVmZiI
```

# <font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">设置</font>
<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">Simple JWT的一些行为可以通过</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">settings.py</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">中的设置变量进行自定义：</font>

```python
# Django project settings.py

from datetime import timedelta
...

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,

    "ALGORITHM": "HS256",
    "SIGNING_KEY": settings.SECRET_KEY,
    "VERIFYING_KEY": "",
    "AUDIENCE": None,
    "ISSUER": None,
    "JSON_ENCODER": None,
    "JWK_URL": None,
    "LEEWAY": 0,

    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",

    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

    "JTI_CLAIM": "jti",

    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),

    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}
```

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">上面显示了这些设置的默认值。</font>

## `<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">ACCESS_TOKEN_LIFETIME</font>`
<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">一个</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">datetime.timedelta</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">对象，指定访问令牌的有效期。 该</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">timedelta</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">值在令牌生成期间添加到当前UTC时间，以获取令牌的默认“ext”声明值。</font>

## `<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">REFRESH_TOKEN_LIFETIME</font>`
<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">一个</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">datetime.timedelta</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">对象，指定刷新令牌的有效期。 在令牌生成期间，此</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">timedelta</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">值被添加到当前UTC时间，以获得令牌的默认“exp”声明值。</font>

## `<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">ROTATE_REFRESH_TOKENS</font>`
<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">当设置为</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">True</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">时，如果向</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">TokenRefreshView</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">提交刷新令牌，则新的刷新令牌将与新的访问令牌一起沿着返回。 这个新的刷新令牌将通过JSON响应中的“refresh”键提供。 新的刷新令牌将具有更新的到期时间，该到期时间通过将</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">REFRESH_TOKEN_LIFETIME</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">设置中的时间增量添加到发出请求的当前时间来确定。 如果正在使用黑名单应用程序，并且</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">BLACKLIST_AFTER_ROTATION</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">设置设置为</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">True</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">，则提交到刷新视图的刷新令牌将添加到黑名单中。</font>

## `<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">BLACKLIST_AFTER_ROTATION</font>`
<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">当设置为</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">True</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">时，如果黑名单应用程序正在使用且</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">TokenRefreshView</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">设置设置为</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">ROTATE_REFRESH_TOKENS</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">，则会将提交给</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">True</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">的刷新令牌添加到黑名单中。您需要在设置文件中将</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">'rest_framework_simplejwt.token_blacklist',</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">添加到</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">INSTALLED_APPS</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">中才能使用此设置。</font>

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">了解更多关于</font>[<font style="color:rgb(41, 128, 185);background-color:rgb(252, 252, 252);">黑名单应用程序</font>](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/blacklist_app.html)<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">。</font>

## `<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">UPDATE_LAST_LOGIN</font>`
<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">当设置为</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">True</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">时，auth_user表中的last_login字段在登录时更新（TokenObtainPairView）。</font>

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">警告：更新last_login将显著增加数据库事务的数量。滥用视图的人可能会降低服务器的速度，这可能是一个安全漏洞。如果你真的想这样做，至少用DRF节流端点。</font>

## `<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">ALGORITHM</font>`
<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">PyJWT库中的算法，将用于对令牌执行签名/验证操作。 为了使用对称HMAC签名和验证，可以使用以下算法：</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">'HS256'</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">、</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">'HS384'</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">、</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">'HS512'</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">。 当选择HMAC算法时，</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">SIGNING_KEY</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">设置将同时用作签名密钥和验证密钥。 在这种情况下，将忽略</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">VERIFYING_KEY</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">设置。 为了使用非对称RSA签名和验证，可以使用以下算法：</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">'RS256'</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">、</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">'RS384'</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">、</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">'RS512'</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">。 选择RSA算法时，必须将</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">SIGNING_KEY</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">设置设置为包含RSA私钥的字符串。 同样，</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">VERIFYING_KEY</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">设置必须设置为包含RSA公钥的字符串。</font>

## `<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">SIGNING_KEY</font>`
<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">用于对生成的令牌的内容进行签名的签名密钥。 对于HMAC签名，这应该是一个随机字符串，其中至少包含签名协议所需的数据位数。 对于RSA签名，这应该是一个包含2048位或更长的RSA私钥的字符串。 由于Simple JWT默认使用256位HMAC签名，因此</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">SIGNING_KEY</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">设置默认为django项目的</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">SECRET_KEY</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">设置值。 虽然这是Simple JWT可以提供的最合理的默认值，但建议开发人员将此设置更改为独立于django项目密钥的值。 这将使更改用于令牌的签名密钥变得更容易，如果它被泄露的话。</font>

## `<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">VERIFYING_KEY</font>`
<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">用于验证生成的令牌内容的验证密钥。 如果HMAC算法已由</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">ALGORITHM</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">设置指定，则将忽略</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">VERIFYING_KEY</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">设置，并使用</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">SIGNING_KEY</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">设置的值。 如果已通过</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">ALGORITHM</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">设置指定RSA算法，则必须将</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">VERIFYING_KEY</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">设置设置为包含RSA公钥的字符串。</font>

## `<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">AUDIENCE</font>`
<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">受众声称被包括在生成的令牌中和/或在解码的令牌中被验证。当设置为</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">None</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">时，此字段将从令牌中排除，并且不进行验证。</font>

## `<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">ISSUER</font>`
<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">发行方声称被包括在生成的令牌中和/或在解码的令牌中被验证。当设置为</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">None</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">时，此字段将从令牌中排除，并且不进行验证。</font>

## `<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">JWK_URL</font>`
<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">JWK_URL用于动态解析验证令牌签名所需的公钥。例如，当使用Auth 0时，您可以将其设置为'</font>[<font style="color:rgb(41, 128, 185);background-color:rgb(252, 252, 252);">https：//yourdomain.auth0.com/.well-known/jwks.json</font>](https://yourdomain.auth0.com/.well-known/jwks.json)<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">'。当设置为</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">None</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">时，此字段将从令牌后端中排除，并且在验证期间不使用。</font>

## `<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">LEEWAY</font>`
<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">Leeway用于为到期时间提供一定的余量。这可以是一个整数秒或</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">datetime.timedelta</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">。更多信息请参考</font>[<font style="color:rgb(41, 128, 185);background-color:rgb(252, 252, 252);">https：//pyjwt.readthedocs.io/en/latest/usage.html#application-time-claim-exp</font>](https://pyjwt.readthedocs.io/en/latest/usage.html#expiration-time-claim-exp)<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">。</font>

## `<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">AUTH_HEADER_TYPES</font>`
<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">需要身份验证的视图将接受的授权标头类型。 例如，值</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">'Bearer'</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">意味着需要身份验证的视图将查找具有以下格式的头：</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">Authorization:</font><font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);"> </font><font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">Bearer</font><font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);"> </font><font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);"><token></font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">。 此设置还可以包含可能的报头类型的列表或元组（例如</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">('Bearer',</font><font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);"> </font><font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">'JWT')</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">）。 如果以这种方式使用列表或元组，并且身份验证失败，则集合中的第一项将用于在响应中构建“WWW-Authenticate”标头。</font>

## `<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">AUTH_HEADER_NAME</font>`
<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">用于身份验证的授权标头名称。默认值是</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">HTTP_AUTHORIZATION</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">，它将接受请求中的</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">Authorization</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">头。例如，如果您想在请求的标题中使用</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">X_Access_Token</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">，请在设置中将</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">AUTH_HEADER_NAME</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">指定为</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">HTTP_X_ACCESS_TOKEN</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">。</font>

## `<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">USER_ID_FIELD</font>`
<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">用户模型中的数据库字段，将包含在生成的令牌中以标识用户。 建议此设置的值指定一个字段，该字段在选定初始值后通常不会更改。 例如，指定“用户名”或“电子邮件”字段将是一个糟糕的选择，因为帐户的用户名或电子邮件可能会根据给定服务中的帐户管理的设计方式而更改。 这可以允许使用旧用户名创建新帐户，而现有令牌仍然有效，使用该用户名作为用户标识符。</font>

## `<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">USER_ID_CLAIM</font>`
<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">生成的令牌中的声明将用于存储用户标识符。例如，设置值</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">'user_id'</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">意味着生成的令牌包括包含用户标识符的“user_id”声明。</font>

## `<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">USER_AUTHENTICATION_RULE</font>`
<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">可调用以确定是否允许用户进行身份验证。此规则在处理有效令牌后应用。用户对象作为参数传递给可调用对象。默认规则是检查</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">is_active</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">标志是否仍为</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">True</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">。可调用对象必须返回一个布尔值，如果已授权，则返回</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">True</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">，否则返回</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">False</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">，结果是一个401状态代码。</font>

## `<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">AUTH_TOKEN_CLASSES</font>`
<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">指向类的点路径列表，这些类指定允许证明身份验证的令牌类型。 更多关于这一点在下面的“令牌类型”部分。</font>

## `<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">TOKEN_TYPE_CLAIM</font>`
<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">用于存储令牌类型的声明名称。 更多关于这一点在下面的“令牌类型”部分。</font>

## `<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">JTI_CLAIM</font>`
<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">用于存储令牌的唯一标识符的声明名称。 此标识符用于标识黑名单应用中已撤销的令牌。在某些情况下，可能需要使用默认“jti”声明之外的另一个声明来存储此类值。</font>

## `<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">TOKEN_USER_CLASS</font>`
<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">由经过验证的令牌支持的无状态用户对象。仅用于JWTStatelessUserAuthentication身份验证后端。该值是指向子类</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">rest_framework_simplejwt.models.TokenUser</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">的虚线路径，这也是默认值。</font>

## `<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">SLIDING_TOKEN_LIFETIME</font>`
<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">一个</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">datetime.timedelta</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">对象，指定滑动令牌在多长时间内有效以证明身份验证。 在令牌生成期间，此</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">timedelta</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">值被添加到当前UTC时间，以获得令牌的默认“exp”声明值。 更多关于这一点在“滑动令牌”下面的部分.</font>

## `<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">SLIDING_TOKEN_REFRESH_LIFETIME</font>`
<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">一个</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">datetime.timedelta</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">对象，指定滑动令牌的刷新有效期。 该</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">timedelta</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">值在令牌生成期间添加到当前UTC时间，以获取令牌的默认“ext”声明值。更多关于这一点在"滑动令牌"下面的部分.</font>

## `<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">SLIDING_TOKEN_REFRESH_EXP_CLAIM</font>`
<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">声明名称，用于存储滑动令牌刷新周期的到期时间。 更多关于这一点在“滑动令牌”下面的部分.</font>

## `<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">CHECK_REVOKE_TOKEN</font>`
<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">如果此字段设置为</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">True</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">，系统将通过比较用户当前密码的md5哈希值与JWT令牌有效负载内的REVOKE_TOKEN_CLAIM字段中存储的值来验证令牌是否已被撤销。</font>

## `<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">REVOKE_TOKEN_CLAIM</font>`
<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">用于存储用户哈希密码的声明名称。如果该REVOKE_TOKEN字段的值是</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">True</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">，则该字段将被包括在JWT有效载荷中。</font>

# <font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">自定义令牌声明</font>
<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">如果您希望自定义由</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">TokenObtainPairView</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">和</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">TokenObtainSlidingView</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">视图生成的Web令牌中包含的声明，请为所需的视图创建一个子类，并为其相应的序列化程序创建一个子类。 以下是如何自定义由</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">TokenObtainPairView</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">生成的令牌中的声明的示例：</font>

```python
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.name
        # ...

        return token
```

```python
# Django project settings.py
...

SIMPLE_JWT = {
    # It will work instead of the default serializer(TokenObtainPairSerializer).
    "TOKEN_OBTAIN_SERIALIZER": "my_app.serializers.MyTokenObtainPairSerializer",
    # ...
}
```

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">请注意，上面的示例将导致自定义声明出现在视图生成的刷新令牌和访问令牌中。 这是因为上面的</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">get_token</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">方法为视图生成刷新令牌，而刷新令牌又用于生成视图的访问令牌。</font>

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">与标准token视图一样，您还需要包含一个指向子类视图的url路由。</font>

# <font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">手动创建令牌</font>
<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">有时，您可能希望手动为用户创建令牌。 这可以通过以下方式实现：</font>

```python
from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
```

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">上面的函数</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">get_tokens_for_user</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">将返回给定用户的新刷新和访问令牌的序列化表示。 一般来说，</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">rest_framework_simplejwt.tokens.Token</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">的任何子类的token都可以通过这种方式创建。</font>

# <font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">令牌类型</font>
<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">Simple JWT提供了两种不同的令牌类型，可用于证明身份验证。 在令牌的有效负载中，其类型可以由其令牌类型声明的值标识，默认情况下为“token_type”。 这可能具有“访问”、“滑动”或“刷新”的值，但是刷新令牌此时不被认为对认证有效。 用于存储类型的声明名称可以通过更改</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">TOKEN_TYPE_CLAIM</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">设置来自定义。</font>

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">默认情况下，Simple JWT需要一个“访问”令牌来证明身份验证。 允许的授权令牌类型由</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">AUTH_TOKEN_CLASSES</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">设置的值确定。 此设置包含指向标记类的点路径列表。 默认情况下，它包含</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">'rest_framework_simplejwt.tokens.AccessToken'</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">点路径，但也可能包含</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">'rest_framework_simplejwt.tokens.SlidingToken'</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">点路径。这两个点路径中的一个或两个都可能出现在auth token类列表中。 如果它们都存在，则这两种令牌类型都可以用于证明认证。</font>

## <font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">滑动令牌</font>
<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">滑动令牌为令牌的用户提供了更方便的体验，其代价是安全性较低，并且在使用黑名单应用程序的情况下，性能较低。 滑动令牌是同时包含过期声明和刷新过期声明的令牌。 只要滑动令牌的过期声明中的时间戳尚未过期，它就可以用来证明身份验证。 此外，只要它的刷新过期声明中的时间戳还没有过去，它也可以被提交到刷新视图，以获得具有更新的过期声明的它自己的另一个副本。</font>

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">如果您想使用滑动令牌，请将</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">AUTH_TOKEN_CLASSES</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">设置更改为</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">('rest_framework_simplejwt.tokens.SlidingToken',)</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">。 （或者，如果您希望允许两种令牌类型都用于身份验证，则</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">AUTH_TOKEN_CLASSES</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">设置可以包括指向</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">AccessToken</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">模块中的</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">SlidingToken</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">和</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">rest_framework_simplejwt.tokens</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">令牌类的点路径。）</font>

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">此外，在访问令牌特定的</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">TokenObtainSlidingView</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">和</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">TokenRefreshSlidingView</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">视图的url旁边或代替访问令牌特定的</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">TokenObtainPairView</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">和</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">TokenRefreshView</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">视图的url，包括用于滑动令牌特定的url：</font>

```python
from rest_framework_simplejwt.views import (
TokenObtainSlidingView,
TokenRefreshSlidingView,
)

urlpatterns = [
    ...
    path('api/token/', TokenObtainSlidingView.as_view(), name='token_obtain'),
    path('api/token/refresh/', TokenRefreshSlidingView.as_view(), name='token_refresh'),
    ...
]
```

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">请注意，如果您使用的是黑名单应用程序，Simple JWT将针对每个经过身份验证的请求，根据黑名单验证所有滑动令牌。 这将降低经过身份验证的API视图的性能。</font>

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">  
</font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);"> </font>

# <font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">黑名单应用程序</font>
<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">Simple JWT包括一个提供令牌黑名单功能的应用程序。 要使用此应用程序，请将其包含在</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">settings.py</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">中的已安装应用程序列表中：</font>

```python
# Django project settings.py

...

INSTALLED_APPS = (
    ...
    'rest_framework_simplejwt.token_blacklist',
...
)
```

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">此外，请确保运行</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">python</font><font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);"> </font><font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">manage.py</font><font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);"> </font><font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">migrate</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">以运行应用程序的迁移。</font>

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">如果在</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">INSTALLED_APPS</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">中检测到黑名单应用程序，Simple JWT会将任何生成的刷新或滑动令牌添加到未完成令牌列表中。 它还将检查任何刷新或滑动令牌是否未出现在令牌黑名单中，然后才认为其有效。</font>

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">Simple JWT黑名单应用程序使用两种模型实现其未完成和黑名单令牌列表：</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">OutstandingToken</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">和</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">BlacklistedToken</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">。 模型管理员是为这两个模型定义的。 要将令牌添加到黑名单中，请在admin中找到其对应的</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">OutstandingToken</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">记录，然后再次使用admin创建指向</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">BlacklistedToken</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">记录的</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">OutstandingToken</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">记录。</font>

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">或者，您可以通过创建</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">BlacklistMixin</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">子类实例并调用实例的</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">blacklist</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">方法来将令牌列入黑名单：</font>

```python
from rest_framework_simplejwt.tokens import RefreshToken

token = RefreshToken(base64_encoded_token_string)
token.blacklist()
```

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">这将为令牌的“jti”声明或</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">JTI_CLAIM</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">设置指定的任何声明创建唯一的未完成令牌和黑名单记录。</font>

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">在</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">urls.py</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">文件中，您还可以包含</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">TokenBlacklistView</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">的路由：</font>

```python
from rest_framework_simplejwt.views import TokenBlacklistView

urlpatterns = [
    ...
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    ...
]
```

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">它允许API用户将发送给</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">/api/token/blacklist/</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">的令牌列入黑名单，例如使用curl：</font>

```python
curl \
-X POST \
-H "Content-Type: application/json" \
-d '{"refresh":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1MDI5NTEwOCwiaWF0IjoxNjUwMjA4NzA4LCJqdGkiOiJhYTY3ZDUxNzkwMGY0MTEyYTY5NTE0MTNmNWQ4NDk4NCIsInVzZXJfaWQiOjF9.tcj1_OcO1BRDfFyw4miHD7mqFdWKxmP7BJDRmxwCzrg"}' \
http://localhost:8000/api/token/blacklist/
```

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">黑名单应用程序还提供了一个管理命令</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">flushexpiredtokens</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">，该命令将删除未完成列表和黑名单中已过期的任何令牌。 您应该在服务器或托管平台上设置一个cron作业，每天运行此命令。</font>

# <font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">无状态用户身份验证</font>
## <font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">JWT StatelessUserAuthentication后端</font>
`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">JWTStatelessUserAuthentication</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">后端的</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">authenticate</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">方法不执行数据库查找以获取用户实例。 相反，它返回一个</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">rest_framework_simplejwt.models.TokenUser</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">实例，它充当一个无状态的用户对象，只由一个经过验证的令牌支持，而不是数据库中的记录。 这可以促进在单独托管的Django应用程序之间开发单点登录功能，这些应用程序都共享相同的令牌密钥。 要使用此功能，请将</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">rest_framework_simplejwt.authentication.JWTStatelessUserAuthentication</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">后端（而不是默认的</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">JWTAuthentication</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">后端）添加到Django REST Framework的</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">DEFAULT_AUTHENTICATION_CLASSES</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">配置设置中：</font>

```python
REST_FRAMEWORK = {
    ...
    'DEFAULT_AUTHENTICATION_CLASSES': (
    ...
    'rest_framework_simplejwt.authentication.JWTStatelessUserAuthentication',
)
...
}
```

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">v5.1.0已将</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">JWTTokenUserAuthentication</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">重命名为</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">JWTStatelessUserAuthentication</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">，但为了向后兼容，支持这两个名称</font>

# `<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">drf-yasg</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">一体化</font>
[<font style="color:rgb(41, 128, 185);background-color:rgb(252, 252, 252);">drf-yasg</font>](https://github.com/axnsan12/drf-yasg)<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">是一个通过检查DRF</font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);"> </font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">Serializer</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">定义自动生成OpenAPI模式的库。因为</font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">django-rest-framework-simplejwt</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">序列化器不是对称的，所以如果您想为JWT令牌端点生成正确的OpenAPI模式，请使用以下代码来修饰您的JWT</font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);"> </font>`<font style="color:rgb(231, 76, 60);background-color:rgb(252, 252, 252);">View</font>`<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">定义。</font>

```python
from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers, status
from rest_framework_simplejwt.views import (
    TokenBlacklistView,
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


class TokenObtainPairResponseSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()


class DecoratedTokenObtainPairView(TokenObtainPairView):
    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: TokenObtainPairResponseSerializer,
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class TokenRefreshResponseSerializer(serializers.Serializer):
    access = serializers.CharField()

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()


class DecoratedTokenRefreshView(TokenRefreshView):
    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: TokenRefreshResponseSerializer,
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class TokenVerifyResponseSerializer(serializers.Serializer):
    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()


class DecoratedTokenVerifyView(TokenVerifyView):
    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: TokenVerifyResponseSerializer,
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class TokenBlacklistResponseSerializer(serializers.Serializer):
    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()


class DecoratedTokenBlacklistView(TokenBlacklistView):
    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: TokenBlacklistResponseSerializer,
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
```

# <font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">rest_framework_simplejwt 包介绍</font>
## <font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">Submodules</font>
## <font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">rest_framework_simplejwt.authentication module</font>
_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">class</font>**_`**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">rest_framework_simplejwt.authentication.</font>**``**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">JWTAuthentication</font>**`**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">(</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">*args</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">,</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">**kwargs</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">)</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">Bases:</font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);"> </font>`**<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">rest_framework.authentication.BaseAuthentication</font>**`

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">An authentication plugin that authenticates requests through a JSON web token provided in a request header.</font>

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">authenticate</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">request: rest_framework.request.Request</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→ Optional[Tuple[AuthUser, rest_framework_simplejwt.tokens.Token]]</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">Authenticate the request and return a two-tuple of (user, token).</font>

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">authenticate_header</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">request: rest_framework.request.Request</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→ str</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">Return a string to be used as the value of the</font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);"> </font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">WWW-Authenticate</font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);"> </font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">header in a</font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);"> </font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">401 Unauthenticated</font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);"> </font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">response, or</font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);"> </font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">None</font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);"> </font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">if the authentication scheme should return</font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);"> </font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">403 Permission Denied</font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);"> </font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">responses.</font>

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">get_header</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">request: rest_framework.request.Request</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→ bytes</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">Extracts the header containing the JSON web token from the given request.</font>

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">get_raw_token</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">header: bytes</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→ Optional[bytes]</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">Extracts an unvalidated JSON web token from the given “Authorization” header value.</font>

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">get_user</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">validated_token: rest_framework_simplejwt.tokens.Token</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→ AuthUser</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">Attempts to find and return a user using the given validated token.</font>

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">get_validated_token</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">raw_token: bytes</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→ rest_framework_simplejwt.tokens.Token</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">Validates an encoded JSON web token and returns a validated token wrapper object.</font>

# <font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">rest_framework_simplejwt包</font>
## <font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">子模块</font>
## <font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">rest_framework_simplejwt.身份验证模块</font>
_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">类</font>**_`**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">rest_framework_simplejwt.authentication.</font>**``**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">JWTAuthentication</font>**`**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">(</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">*args</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">,</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">**kwargs</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">)</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">底座：</font>`**<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">rest_framework.authentication.BaseAuthentication</font>**`

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">一个身份验证插件，通过请求头中提供的JSON Web令牌对请求进行身份验证。</font>

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">authenticate</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">request：rest_framework.request.Request</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→可选[Tuple[AuthUser，rest_framework_simplejwt.tokens.Token]]</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">验证请求并返回一个二元组（user，token）。</font>

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">authenticate_header</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">request：rest_framework.request.Request</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→应力</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">返回一个字符串，用作</font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">401 Unauthenticated</font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">响应中的</font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">WWW-Authenticate</font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">标头的值;如果身份验证方案应返回</font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">403 Permission Denied</font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">响应，则返回</font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">None</font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">。</font>

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">get_header</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">request：rest_framework.request.Request</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→字节</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">从给定请求中提取包含JSON Web令牌的标头。</font>

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">get_raw_token</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">头：字节</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→可选[字节]</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">从给定的“Authorization”头值中提取未经验证的JSON Web令牌。</font>

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">get_user</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">validated_token：rest_framework_simplejwt.tokens.Token</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→ AuthUser</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">尝试使用给定的验证令牌查找并返回用户。</font>

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">get_validated_token</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">raw_token：字节</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→ rest_framework_simplejwt.tokens.Token</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">验证已编码的JSON Web令牌并返回已验证的令牌包装器对象。</font>

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">media_type</font>**`_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">= 'application/json'</font>**_

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">www_authenticate_realm</font>**`_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">= 'API'</font>**_

_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">类</font>**_`**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">rest_framework_simplejwt.authentication.</font>**``**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">JWTStatelessUserAuthentication</font>**`**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">(</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">*args</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">,</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">**kwargs</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">)</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">底座：</font>[<font style="color:rgb(41, 128, 185);background-color:rgb(252, 252, 252);">rest_framework_simplejwt.authentication.JWTAuthentication</font>](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/rest_framework_simplejwt.html#rest_framework_simplejwt.authentication.JWTAuthentication)

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">一种身份验证插件，通过请求头中提供的JSON Web令牌对请求进行身份验证，而不执行数据库查找以获取用户实例。</font>

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">get_user</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">validated_token：rest_framework_simplejwt.tokens.Token</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→ AuthUser</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">返回一个无状态的用户对象，该对象由给定的已验证令牌支持。</font>

`**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">rest_framework_simplejwt.authentication.</font>**``**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">JWTTokenUserAuthentication</font>**`

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">别名：</font>[<font style="color:rgb(41, 128, 185);background-color:rgb(252, 252, 252);">rest_framework_simplejwt.authentication.JWTStatelessUserAuthentication</font>](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/rest_framework_simplejwt.html#rest_framework_simplejwt.authentication.JWTStatelessUserAuthentication)

`**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">rest_framework_simplejwt.authentication.</font>**``**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">default_user_authentication_rule</font>**`**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">(</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">用户：AuthUser</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">)</font>****<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">→ bool</font>**

## <font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">rest_framework_simplejwt.models模块</font>
_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">类</font>**_`**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">rest_framework_simplejwt.models.</font>**``**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">TokenUser</font>**`**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">(</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">token：Token</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">)</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">底座：</font>[<font style="color:rgb(41, 128, 185);background-color:rgb(252, 252, 252);">object</font>](https://docs.python.org/3.8/library/functions.html#object)

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">一个模仿django.contrib.auth.models.AncientousUser的虚拟用户类。与</font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">JWTStatelessUserAuthentication</font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">后端结合使用，以跨共享相同密钥的服务实现单点登录功能。</font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);"> </font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">JWTStatelessUserAuthentication</font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">将返回此类的实例，而不是</font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">User</font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">模型实例。 该类的对象充当无状态用户对象，由经过验证的令牌支持。</font>

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">check_password</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">raw_password：str</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→无</font>**

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">delete</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→无</font>**

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">get_all_permissions</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">obj：Optional[object] = None</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→设置</font>**

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">get_group_permissions</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">obj：Optional[object] = None</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→设置</font>**

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">get_username</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→应力</font>**

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">groups</font>**`

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">has_module_perms</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">模块：str</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→ bool</font>**

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">has_perm</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">perm：str</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">,</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">obj：Optional[object] = None</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→ bool</font>**

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">has_perms</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">perm_list：List[str]，obj：Optional[object] = None</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→ bool</font>**

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">id</font>**`

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">is_active</font>**`_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">= True</font>**_

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">is_anonymous</font>**`

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">is_authenticated</font>**`

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">is_staff</font>**`

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">is_superuser</font>**`

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">pk</font>**`

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">save</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→无</font>**

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">set_password</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">raw_password：str</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→无</font>**

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">user_permissions</font>**`

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">username</font>**`

## <font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">rest_framework_simplejwt.serializers模块</font>
_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">类</font>**_`**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">rest_framework_simplejwt.serializers.</font>**``**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">PasswordField</font>**`**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">(</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">*args</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">,</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">**kwargs</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">)</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">底座：</font>`**<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">rest_framework.authentication.BaseAuthentication</font>**`

_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">类</font>**_`**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">rest_framework_simplejwt.serializers.</font>**``**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">TokenBlacklistSerializer</font>**`**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">(</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">实例=无</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">,</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">data= class 'rest_framework.fields.empty'></font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">,</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">**kwargs</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">)</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">底座：</font>`**<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">rest_framework.authentication.BaseAuthentication</font>**`

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">token_class</font>**`

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">别名：</font>[<font style="color:rgb(41, 128, 185);background-color:rgb(252, 252, 252);">rest_framework_simplejwt.tokens.RefreshToken</font>](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/rest_framework_simplejwt.html#rest_framework_simplejwt.tokens.RefreshToken)

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">validate</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">attrs：Dict[str，Any]</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→ Dict[任意，任意]</font>**

_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">类</font>**_`**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">rest_framework_simplejwt.serializers.</font>**``**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">TokenObtainPairSerializer</font>**`**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">(</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">*args</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">,</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">**kwargs</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">)</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">底座：</font>[<font style="color:rgb(41, 128, 185);background-color:rgb(252, 252, 252);">rest_framework_simplejwt.serializers.TokenObtainSerializer</font>](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/rest_framework_simplejwt.html#rest_framework_simplejwt.serializers.TokenObtainSerializer)

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">token_class</font>**`

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">别名：</font>[<font style="color:rgb(41, 128, 185);background-color:rgb(252, 252, 252);">rest_framework_simplejwt.tokens.RefreshToken</font>](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/rest_framework_simplejwt.html#rest_framework_simplejwt.tokens.RefreshToken)

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">validate</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">attrs：Dict[str，Any]</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→ Dict[str，str]</font>**

_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">类</font>**_`**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">rest_framework_simplejwt.serializers.</font>**``**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">TokenObtainSerializer</font>**`**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">(</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">*args</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">,</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">**kwargs</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">)</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">底座：</font>`**<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">rest_framework.authentication.BaseAuthentication</font>**`

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">default_error_messages</font>**`_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">=“no_active_account”：“找不到具有给定凭据的活动帐户”}</font>**_

_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">classmethod</font>**_`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">get_token</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">用户：AuthUser</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→ rest_framework_simplejwt.tokens.Token</font>**

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">token_class</font>**`_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">=无</font>**_

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">username_field</font>**`_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">= '用户名'</font>**_

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">validate</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">attrs：Dict[str，Any]</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→ Dict[任意，任意]</font>**

_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">类</font>**_`**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">rest_framework_simplejwt.serializers.</font>**``**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">TokenObtainSlidingSerializer</font>**`**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">(</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">*args</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">,</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">**kwargs</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">)</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">底座：</font>[<font style="color:rgb(41, 128, 185);background-color:rgb(252, 252, 252);">rest_framework_simplejwt.serializers.TokenObtainSerializer</font>](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/rest_framework_simplejwt.html#rest_framework_simplejwt.serializers.TokenObtainSerializer)

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">token_class</font>**`

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">别名：</font>[<font style="color:rgb(41, 128, 185);background-color:rgb(252, 252, 252);">rest_framework_simplejwt.tokens.SlidingToken</font>](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/rest_framework_simplejwt.html#rest_framework_simplejwt.tokens.SlidingToken)

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">validate</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">attrs：Dict[str，Any]</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→ Dict[str，str]</font>**

_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">类</font>**_`**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">rest_framework_simplejwt.serializers.</font>**``**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">TokenRefreshSerializer</font>**`**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">(</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">实例=无</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">,</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">data= class 'rest_framework.fields.empty'></font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">,</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">**kwargs</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">)</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">底座：</font>`**<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">rest_framework.authentication.BaseAuthentication</font>**`

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">token_class</font>**`

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">别名：</font>[<font style="color:rgb(41, 128, 185);background-color:rgb(252, 252, 252);">rest_framework_simplejwt.tokens.RefreshToken</font>](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/rest_framework_simplejwt.html#rest_framework_simplejwt.tokens.RefreshToken)

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">validate</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">attrs：Dict[str，Any]</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→ Dict[str，str]</font>**

_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">类</font>**_`**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">rest_framework_simplejwt.serializers.</font>**``**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">TokenRefreshSlidingSerializer</font>**`**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">(</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">实例=无</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">,</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">data= class 'rest_framework.fields.empty'></font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">,</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">**kwargs</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">)</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">底座：</font>`**<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">rest_framework.authentication.BaseAuthentication</font>**`

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">token_class</font>**`

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">别名：</font>[<font style="color:rgb(41, 128, 185);background-color:rgb(252, 252, 252);">rest_framework_simplejwt.tokens.SlidingToken</font>](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/rest_framework_simplejwt.html#rest_framework_simplejwt.tokens.SlidingToken)

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">validate</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">attrs：Dict[str，Any]</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→ Dict[str，str]</font>**

_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">类</font>**_`**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">rest_framework_simplejwt.serializers.</font>**``**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">TokenVerifySerializer</font>**`**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">(</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">实例=无</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">,</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">data= class 'rest_framework.fields.empty'></font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">,</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">**kwargs</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">)</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">底座：</font>`**<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">rest_framework.authentication.BaseAuthentication</font>**`

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">validate</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">attrs：Dict[str，None]</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→ Dict[任意，任意]</font>**

## <font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">rest_framework_simplejwt.tokens模块</font>
_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">类</font>**_`**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">rest_framework_simplejwt.tokens.</font>**``**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">AccessToken</font>**`**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">(</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">token：Optional[Token] = None</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">,</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">验证：bool = True</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">)</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">底座：</font>[<font style="color:rgb(41, 128, 185);background-color:rgb(252, 252, 252);">rest_framework_simplejwt.tokens.Token</font>](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/rest_framework_simplejwt.html#rest_framework_simplejwt.tokens.Token)

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">lifetime</font>**`_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">= datetime.timedelta（秒=300）</font>**_

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">token_type</font>**`_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">= 'access'</font>**_

_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">类</font>**_`**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">rest_framework_simplejwt.tokens.</font>**``**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">BlacklistMixin</font>**`

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">底座：</font>[<font style="color:rgb(41, 128, 185);background-color:rgb(252, 252, 252);">object</font>](https://docs.python.org/3.8/library/functions.html#object)

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">如果将</font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">rest_framework_simplejwt.token_blacklist</font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">应用配置为使用，则从</font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">BlacklistMixin</font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">子类创建的令牌将自己插入未完成令牌列表中，并检查其在令牌黑名单中的成员资格。</font>

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">blacklist</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→ rest_framework_simplejwt.token_blacklist.models. BlackBundToken</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">确保此令牌包含在未完成令牌列表中并将其添加到黑名单。</font>

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">check_blacklist</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→无</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">检查此令牌是否存在于令牌黑名单中。 如果是，则引发</font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">TokenError</font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">。</font>

_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">classmethod</font>**_`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">for_user</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">用户：AuthUser</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→ rest_framework_simplejwt.tokens.Token</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">将此令牌添加到未完成令牌列表中。</font>

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">verify</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">*args</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">,</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">**kwargs</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→无</font>**

_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">类</font>**_`**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">rest_framework_simplejwt.tokens.</font>**``**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">RefreshToken</font>**`**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">(</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">token：Optional[Token] = None</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">,</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">验证：bool = True</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">)</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">底座：</font>[<font style="color:rgb(41, 128, 185);background-color:rgb(252, 252, 252);">1#</font>](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/rest_framework_simplejwt.html#rest_framework_simplejwt.tokens.BlacklistMixin)<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">、</font>[<font style="color:rgb(41, 128, 185);background-color:rgb(252, 252, 252);">2#</font>](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/rest_framework_simplejwt.html#rest_framework_simplejwt.tokens.Token)

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">access_token</font>**`

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">返回从此刷新令牌创建的访问令牌。 将此刷新令牌中存在的所有声明复制到新的访问令牌，但</font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">no_copy_claims</font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">属性中列出的声明除外。</font>

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">access_token_class</font>**`

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">别名：</font>[<font style="color:rgb(41, 128, 185);background-color:rgb(252, 252, 252);">AccessToken</font>](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/rest_framework_simplejwt.html#rest_framework_simplejwt.tokens.AccessToken)

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">lifetime</font>**`_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">= datetime.timedelta（days=1）</font>**_

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">no_copy_claims</font>**`_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">=（'token_type'，'exp'，' jti'，'jti'）</font>**_

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">token_type</font>**`_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">= '刷新'</font>**_

_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">类</font>**_`**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">rest_framework_simplejwt.tokens.</font>**``**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">SlidingToken</font>**`**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">(</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">*args</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">,</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">**kwargs</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">)</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">底座：</font>[<font style="color:rgb(41, 128, 185);background-color:rgb(252, 252, 252);">1#</font>](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/rest_framework_simplejwt.html#rest_framework_simplejwt.tokens.BlacklistMixin)<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">、</font>[<font style="color:rgb(41, 128, 185);background-color:rgb(252, 252, 252);">2#</font>](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/rest_framework_simplejwt.html#rest_framework_simplejwt.tokens.Token)

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">lifetime</font>**`_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">= datetime.timedelta（秒=300）</font>**_

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">token_type</font>**`_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">= 'sliding'</font>**_

_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">类</font>**_`**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">rest_framework_simplejwt.tokens.</font>**``**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">Token</font>**`**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">(</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">token：Optional[Token] = None</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">,</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">验证：bool = True</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">)</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">底座：</font>[<font style="color:rgb(41, 128, 185);background-color:rgb(252, 252, 252);">object</font>](https://docs.python.org/3.8/library/functions.html#object)

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">一个验证和包装现有JWT或可用于构建新JWT的类。</font>

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">check_exp</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">声明：str = 'exp'</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">,</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">current_time：可选[datetime.datetime] =无</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→无</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">检查给定声明中的时间戳值是否已经过去（自</font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">current_time</font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">中给定的datetime值以来）。 如果是，则引发带有面向用户的错误消息的TokenError。</font>

_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">classmethod</font>**_`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">for_user</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">用户：AuthUser</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→ rest_framework_simplejwt.tokens.Token</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">返回给定用户的授权令牌，该令牌将在对用户凭据进行身份验证后提供。</font>

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">get</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">关键字：字符串</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">,</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">默认值：可选[任何] =无</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→任何</font>**

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">get_token_backend</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">TokenBackend的</font>**

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">lifetime</font>**`_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">=无</font>**_

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">set_exp</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">声明：str = 'exp'</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">,</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">from_time：可选[datetime.datetime] =无</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">,</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">lifetime：Optional[datetime.timedelta] = None</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→无</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">更新令牌的过期时间。</font>

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">请参见：</font>[<font style="color:rgb(41, 128, 185);background-color:rgb(252, 252, 252);">https：//tools.ietf.org/html/rfc7519#section-4.1.4</font>](https://tools.ietf.org/html/rfc7519#section-4.1.4)

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">set_iat</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">声明：str = 'iat'</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">,</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">at_time：可选[datetime.datetime] =无</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→无</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">更新颁发令牌的时间。</font>

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">请参见：</font>[<font style="color:rgb(41, 128, 185);background-color:rgb(252, 252, 252);">https：//tools.ietf.org/html/rfc7519#section-4.1.6</font>](https://tools.ietf.org/html/rfc7519#section-4.1.6)

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">set_jti</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→无</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">使用字符串填充令牌的已配置jti声明，其中稍后选择相同字符串的概率可以忽略。</font>

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">请参见：</font>[<font style="color:rgb(41, 128, 185);background-color:rgb(252, 252, 252);">https：//tools.ietf.org/html/rfc7519#section-4.1.7</font>](https://tools.ietf.org/html/rfc7519#section-4.1.7)

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">token_backend</font>**`

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">token_type</font>**`_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">=无</font>**_

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">verify</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→无</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">执行解码此令牌时未执行的其他验证步骤。 此方法是“公共”API的一部分，以表明它可以在子类中被重写。</font>

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">verify_token_type</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→无</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">确保令牌类型声明存在并且具有正确的值。</font>

_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">类</font>**_`**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">rest_framework_simplejwt.tokens.</font>**``**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">UntypedToken</font>**`**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">(</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">token：Optional[Token] = None</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">,</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">验证：bool = True</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">)</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">底座：</font>[<font style="color:rgb(41, 128, 185);background-color:rgb(252, 252, 252);">rest_framework_simplejwt.tokens.Token</font>](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/rest_framework_simplejwt.html#rest_framework_simplejwt.tokens.Token)

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">lifetime</font>**`_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">= datetime.timedelta（0）</font>**_

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">token_type</font>**`_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">= 'untyped'</font>**_

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">verify_token_type</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→无</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">未类型化的令牌不会验证“token_type”声明。 这在对令牌的签名和其他与令牌的预期用途无关的属性执行常规验证时很有用。</font>

## <font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">rest_framework_simplejwt.utils模块</font>
`**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">rest_framework_simplejwt.utils.</font>**``**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">aware_utcnow</font>**`**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">(</font>****<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">)</font>****<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">→ datetime.datetime</font>**

`**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">rest_framework_simplejwt.utils.</font>**``**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">datetime_from_epoch</font>**`**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">(</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">ts：浮动</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">)</font>****<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">→ datetime.datetime</font>**

`**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">rest_framework_simplejwt.utils.</font>**``**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">datetime_to_epoch</font>**`**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">(</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">dt：datetime.datetime</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">)</font>****<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">→ int</font>**

`**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">rest_framework_simplejwt.utils.</font>**``**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">format_lazy</font>**`**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">(</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">s：str</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">,</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">*args</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">,</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">**kwargs</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">)</font>****<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">→应力</font>**

`**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">rest_framework_simplejwt.utils.</font>**``**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">get_md5_hash_password</font>**`**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">(</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">密码：str</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">)</font>****<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">→应力</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">返回给定密码的MD5哈希值</font>

`**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">rest_framework_simplejwt.utils.</font>**``**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">make_utc</font>**`**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">(</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">dt：datetime.datetime</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">)</font>****<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">→ datetime.datetime</font>**

## <font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">rest_framework_simplejwt.views模块</font>
_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">类</font>**_`**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">rest_framework_simplejwt.views.</font>**``**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">TokenBlacklistView</font>**`**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">(</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">**kwargs</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">)</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">底座：</font>[<font style="color:rgb(41, 128, 185);background-color:rgb(252, 252, 252);">rest_framework_simplejwt.views.TokenViewBase</font>](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/rest_framework_simplejwt.html#rest_framework_simplejwt.views.TokenViewBase)

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">获取令牌并将其列入黑名单。必须与安装的</font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">rest_framework_simplejwt.token_blacklist</font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">应用一起使用。</font>

_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">类</font>**_`**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">rest_framework_simplejwt.views.</font>**``**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">TokenObtainPairView</font>**`**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">(</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">**kwargs</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">)</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">底座：</font>[<font style="color:rgb(41, 128, 185);background-color:rgb(252, 252, 252);">rest_framework_simplejwt.views.TokenViewBase</font>](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/rest_framework_simplejwt.html#rest_framework_simplejwt.views.TokenViewBase)

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">获取一组用户凭据并返回访问和刷新JSON Web令牌对，以证明这些凭据的身份验证。</font>

_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">类</font>**_`**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">rest_framework_simplejwt.views.</font>**``**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">TokenObtainSlidingView</font>**`**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">(</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">**kwargs</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">)</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">底座：</font>[<font style="color:rgb(41, 128, 185);background-color:rgb(252, 252, 252);">rest_framework_simplejwt.views.TokenViewBase</font>](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/rest_framework_simplejwt.html#rest_framework_simplejwt.views.TokenViewBase)

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">获取一组用户凭据并返回一个滑动JSON Web令牌来证明这些凭据的身份验证。</font>

_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">类</font>**_`**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">rest_framework_simplejwt.views.</font>**``**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">TokenRefreshSlidingView</font>**`**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">(</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">**kwargs</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">)</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">底座：</font>[<font style="color:rgb(41, 128, 185);background-color:rgb(252, 252, 252);">rest_framework_simplejwt.views.TokenViewBase</font>](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/rest_framework_simplejwt.html#rest_framework_simplejwt.views.TokenViewBase)

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">获取滑动JSON Web令牌，如果令牌的刷新周期尚未到期，则返回新的刷新版本。</font>

_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">类</font>**_`**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">rest_framework_simplejwt.views.</font>**``**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">TokenRefreshView</font>**`**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">(</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">**kwargs</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">)</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">底座：</font>[<font style="color:rgb(41, 128, 185);background-color:rgb(252, 252, 252);">rest_framework_simplejwt.views.TokenViewBase</font>](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/rest_framework_simplejwt.html#rest_framework_simplejwt.views.TokenViewBase)

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">获取刷新类型JSON Web令牌，如果刷新令牌有效，则返回访问类型JSON Web令牌。</font>

_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">类</font>**_`**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">rest_framework_simplejwt.views.</font>**``**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">TokenVerifyView</font>**`**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">(</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">**kwargs</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">)</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">底座：</font>[<font style="color:rgb(41, 128, 185);background-color:rgb(252, 252, 252);">rest_framework_simplejwt.views.TokenViewBase</font>](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/rest_framework_simplejwt.html#rest_framework_simplejwt.views.TokenViewBase)

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">接受一个令牌并指示它是否有效。 此视图不提供有关令牌是否适合特定用途的信息。</font>

_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">类</font>**_`**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">rest_framework_simplejwt.views.</font>**``**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">TokenViewBase</font>**`**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">(</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">**kwargs</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">)</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">底座：</font>`**<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">rest_framework.authentication.BaseAuthentication</font>**`

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">authentication_classes</font>**`_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">= ()</font>**_

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">get_authenticate_header</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">request：rest_framework.request.Request</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→应力</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">如果请求未经身份验证，请确定用于401响应的WWW-Authenticate标头（如果有）。</font>

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">get_serializer_class</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→ rest_framework.serializers.Serializer</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">如果设置了serializer_class，则直接使用它。否则从设置中获取类。</font>

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">permission_classes</font>**`_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">= ()</font>**_

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">post</font>**`**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">(</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">request：rest_framework.request.Request</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">,</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">*args</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">,</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">**kwargs</font>**_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">)</font>****<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">→ rest_framework.response.Response</font>**

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">serializer_class</font>**`_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">=无</font>**_

`**<font style="color:rgb(0, 0, 0);background-color:rgb(240, 240, 240);">www_authenticate_realm</font>**`_**<font style="color:rgb(85, 85, 85);background-color:rgb(240, 240, 240);">= 'API'</font>**_

`**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">rest_framework_simplejwt.views.</font>**``**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">token_blacklist</font>**`**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">(</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">请求</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">,</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">*args</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">,</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">**kwargs</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">)</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">获取令牌并将其列入黑名单。必须与安装的</font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">rest_framework_simplejwt.token_blacklist</font><font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">应用一起使用。</font>

`**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">rest_framework_simplejwt.views.</font>**``**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">token_obtain_pair</font>**`**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">(</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">请求</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">,</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">*args</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">,</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">**kwargs</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">)</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">获取一组用户凭据并返回访问和刷新JSON Web令牌对，以证明这些凭据的身份验证。</font>

`**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">rest_framework_simplejwt.views.</font>**``**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">token_obtain_sliding</font>**`**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">(</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">请求</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">,</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">*args</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">,</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">**kwargs</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">)</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">获取一组用户凭据并返回一个滑动JSON Web令牌来证明这些凭据的身份验证。</font>

`**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">rest_framework_simplejwt.views.</font>**``**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">token_refresh</font>**`**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">(</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">请求</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">,</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">*args</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">,</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">**kwargs</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">)</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">获取刷新类型JSON Web令牌，如果刷新令牌有效，则返回访问类型JSON Web令牌。</font>

`**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">rest_framework_simplejwt.views.</font>**``**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">token_refresh_sliding</font>**`**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">(</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">请求</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">,</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">*args</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">,</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">**kwargs</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">)</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">获取滑动JSON Web令牌，如果令牌的刷新周期尚未到期，则返回新的刷新版本。</font>

`**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">rest_framework_simplejwt.views.</font>**``**<font style="color:rgb(0, 0, 0);background-color:rgb(231, 242, 250);">token_verify</font>**`**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">(</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">请求</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">,</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">*args</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">,</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">**kwargs</font>**_**<font style="color:rgb(41, 128, 185);background-color:rgb(231, 242, 250);">)</font>**

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">接受一个令牌并指示它是否有效。 此视图不提供有关令牌是否适合特定用途的信息。</font>

