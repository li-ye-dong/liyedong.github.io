## <font style="color:rgb(39, 38, 43);">什么是认证(Authentication)？</font>
<font style="color:rgb(92, 89, 98);">身份验证是将传入的请求对象(request)与一组标识凭据（例如用户名+密码或者令牌token）相关联的机制。REST framework 提供了一些开箱即用的身份验证方案，并且还允许你实现自定义方案。</font>

<font style="color:rgb(92, 89, 98);">DRF的每个认证方案实际上是一个类。你可以在视图中使用一个或多个认证方案类。REST framework 将尝试使用列表中的每个类进行身份验证，并使用成功完成验证的第一个类的返回的元组设置</font><font style="color:rgb(92, 89, 98);"> </font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">request.user</font>`<font style="color:rgb(92, 89, 98);"> </font><font style="color:rgb(92, 89, 98);">和</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">request.auth</font>`<font style="color:rgb(92, 89, 98);">。</font>

<font style="color:rgb(92, 89, 98);">用户通过认证后</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">request.user</font>`<font style="color:rgb(92, 89, 98);">返回Django的User实例，否则返回</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">AnonymousUser</font>`<font style="color:rgb(92, 89, 98);">的实例。</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">request.auth</font>`<font style="color:rgb(92, 89, 98);">通常为None。如果使用token认证，</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">request.auth</font>`<font style="color:rgb(92, 89, 98);">可以包含认证过的token。</font>

**<font style="color:rgb(92, 89, 98);">注</font>**<font style="color:rgb(92, 89, 98);">：认证一般发生在权限校验之前。</font>

## <font style="color:rgb(39, 38, 43);">DRF自带认证方案</font>
<font style="color:rgb(92, 89, 98);">Django REST Framework提供了如下几种认证方案:</font>

+ <font style="color:rgb(92, 89, 98);">Session认证</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">SessionAuthentication</font>`<font style="color:rgb(92, 89, 98);">类：此认证方案使用Django的默认session后端进行身份验证。当客户端发送登录请求通过验证后，Django通过session将用户信息存储在服务器中保持用户的请求状态。Session身份验证适用于与你的网站在相同的Session环境中运行的AJAX客户端 (注：这也是Session认证的最大弊端)。</font>
+ <font style="color:rgb(92, 89, 98);">基本认证</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">BasicAuthentication</font>`<font style="color:rgb(92, 89, 98);">类：此认证方案使用HTTP 基本认证，针对用户的用户名和密码进行认证。使用这种方式后浏览器会跳出登录框让用户输入用户名和密码认证。基本认证通常只适用于测试。</font>
+ <font style="color:rgb(92, 89, 98);">远程认证</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">RemoteUserAuthentication</font>`<font style="color:rgb(92, 89, 98);">类：此认证方案为用户名不存在的用户自动创建用户实例。这个很少用，具体见文档。</font>
+ <font style="color:rgb(92, 89, 98);">Token认证</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">TokenAuthentication</font>`<font style="color:rgb(92, 89, 98);">类：该认证方案是DRF提供的使用简单的基于Token的HTTP认证方案。当客户端发送登录请求时，服务器便会生成一个Token并将此Token返回给客户端，作为客户端进行请求的一个标识以后客户端只需带上这个Token前来请求数据即可，无需再次带上用户名和密码。后面我们会详细介绍如何使用这种认证方案。</font>

**<font style="color:rgb(92, 89, 98);">注意</font>**<font style="color:rgb(92, 89, 98);">：如果你在生产环境下使用</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">BasicAuthentication</font>`<font style="color:rgb(92, 89, 98);">和</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">TokenAuthentication</font>`<font style="color:rgb(92, 89, 98);">认证，你必须确保你的API仅在</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">https</font>`<font style="color:rgb(92, 89, 98);">可用。</font>

## <font style="color:rgb(39, 38, 43);">如何在DRF中设置认证方案?</font>
### <font style="color:rgb(39, 38, 43);">设置默认的全局认证方案</font>
```python
# settings.py

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )}
```

### <font style="color:rgb(39, 38, 43);">在基于类的视图(CBV)中使用</font>
```python
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class ExampleView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
```

### <font style="color:rgb(39, 38, 43);">在基于函数的视图中使用</font>
```python
from rest_framework.decorators import api_view, authentication_classes, permission_classes

@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def example_view(request, format=None):
    content = {
        'user': unicode(request.user),  # `django.contrib.auth.User` 实例。
        'auth': unicode(request.auth),  # None
    }
    return Response(content)
```

## <font style="color:rgb(39, 38, 43);">如何自定义认证方案?</font>
<font style="color:rgb(92, 89, 98);">要实现自定义的认证方案，首先要继承</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">BaseAuthentication</font>`<font style="color:rgb(92, 89, 98);">类并且重写</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">.authenticate(self, request)</font>`<font style="color:rgb(92, 89, 98);">方法。如果认证成功，该方法应返回</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">(user, auth)</font>`<font style="color:rgb(92, 89, 98);">的二元元组，否则返回</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">None</font>`<font style="color:rgb(92, 89, 98);">。</font>

<font style="color:rgb(92, 89, 98);">在某些情况下，你可能不想返回</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">None</font>`<font style="color:rgb(92, 89, 98);">，而是希望从</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">.authenticate()</font>`<font style="color:rgb(92, 89, 98);">方法抛出</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">AuthenticationFailed</font>`<font style="color:rgb(92, 89, 98);">异常。通常你应该采取的方法是：</font>

+ <font style="color:rgb(92, 89, 98);">如果不尝试验证，返回</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">None</font>`<font style="color:rgb(92, 89, 98);">。还将检查任何其他正在使用的身份验证方案。</font>
+ <font style="color:rgb(92, 89, 98);">如果尝试验证但失败，则抛出</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">AuthenticationFailed</font>`<font style="color:rgb(92, 89, 98);">异常。无论任何权限检查也不检查任何其他身份验证方案，立即返回错误响应。</font>

<font style="color:rgb(92, 89, 98);">你也可以重写</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">.authenticate_header(self, request)</font>`<font style="color:rgb(92, 89, 98);">方法。如果实现该方法，则应返回一个字符串，该字符串将用作</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">HTTP 401 Unauthorized</font>`<font style="color:rgb(92, 89, 98);">响应中的</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">WWW-Authenticate</font>`<font style="color:rgb(92, 89, 98);">头的值。如果</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">.authenticate_header()</font>`<font style="color:rgb(92, 89, 98);">方法未被重写，则认证方案将在未验证的请求被拒绝访问时返回</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">HTTP 403 Forbidden</font>`<font style="color:rgb(92, 89, 98);">响应。</font>

### <font style="color:rgb(39, 38, 43);">示例</font>
<font style="color:rgb(92, 89, 98);">以下示例将以自定义请求标头中名称为’X_USERNAME’提供的用户名作为用户对任何传入请求进行身份验证，其它类似自定义认证需求比如支持用户同时按用户名或email进行验证。</font>

```python
from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions


class ExampleAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        username = request.META.get('X_USERNAME')
        if not username:
            return None

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, None)
```

## <font style="color:rgb(39, 38, 43);">前后端分离时为何推荐token认证？</font>
+ <font style="color:rgb(92, 89, 98);">Token无需存储降低服务器成本，session是将用户信息存储在服务器中的，当用户量增大时服务器的压力也会随着增大。</font>
+ <font style="color:rgb(92, 89, 98);">防御CSRF跨站伪造请求攻击，session是基于cookie进行用户识别的, cookie如果被截获，用户信息就容易泄露。</font>
+ <font style="color:rgb(92, 89, 98);">扩展性强，session需要存储无法共享，当搭建了多个服务器时其他服务器无法获取到session中的验证数据用户无法验证成功。Token可以实现服务器间共享，这样不管哪里都可以访问到。</font>
+ <font style="color:rgb(92, 89, 98);">Token可以减轻服务器的压力，减少频繁的查询数据库。</font>
+ <font style="color:rgb(92, 89, 98);">支持跨域访问, 适用于移动平台应用</font>

## <font style="color:rgb(39, 38, 43);">如何使用TokenAuthentication</font>
<font style="color:rgb(92, 89, 98);">DRF自带的</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">TokenAuthentication</font>`<font style="color:rgb(92, 89, 98);">方案可以实现基本的token认证，整个流程如下：</font>

<font style="color:rgb(92, 89, 98);">首先，你需要将修改</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">settings.py</font>`<font style="color:rgb(92, 89, 98);">, 加入如下app。</font>

```python
INSTALLED_APPS = (
    ...
    'rest_framework.authtoken'
)
```

<font style="color:rgb(92, 89, 98);">其次，你需要为你的用户生成令牌(token)。如果你希望在创建用户时自动生成token，你可以借助Django的信号(signals)实现，如下所示：</font>

```python
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
```

<font style="color:rgb(92, 89, 98);">如果你已经创建了一些用户，则可以打开shell为所有现有用户生成令牌，如下所示：</font>

```python
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


for user in User.objects.all():    
    Token.objects.get_or_create(user=user)
```

<font style="color:rgb(92, 89, 98);">你还可以在</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">admin.py</font>`<font style="color:rgb(92, 89, 98);">中给用户创建token，如下所示：</font>

```python
from rest_framework.authtoken.admin import TokenAdmin
TokenAdmin.raw_id_fields = ['user']
```

<font style="color:rgb(92, 89, 98);">从3.6.4起，你还可以使用如下命令为一个指定用户新建或重置token。</font>

```python
./manage.py drf_create_token <username> # 新建
./manage.py drf_create_token -r <username> # 重置
```

<font style="color:rgb(92, 89, 98);">接下来，你需要暴露用户获取token的url地址(API端点).</font>

```python
from rest_framework.authtoken import views
urlpatterns += [
    url(r'^api-token-auth/', views.obtain_auth_token)]
```

<font style="color:rgb(92, 89, 98);">这样每当用户使用form表单或JSON将有效的</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">username</font>`<font style="color:rgb(92, 89, 98);">和</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">password</font>`<font style="color:rgb(92, 89, 98);">字段POST提交到以上视图时，</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">obtain_auth_token</font>`<font style="color:rgb(92, 89, 98);">视图将返回如下JSON响应：</font>

```python
{ 'token' : '9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b' }
```

<font style="color:rgb(92, 89, 98);">客户端拿到token后可以将其存储到本地cookie或localstorage里，下次发送请求时把token包含在</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">Authorization</font>``<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);"> </font>`<font style="color:rgb(92, 89, 98);">HTTP头即可，如下所示：</font>

```python
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

<font style="color:rgb(92, 89, 98);">你还可以通过curl工具来进行简单测试。</font>

```python
curl -X GET http://127.0.0.1:8000/api/example/ -H 'Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'
```

### <font style="color:rgb(39, 38, 43);">自定义Token返回信息</font>
<font style="color:rgb(92, 89, 98);">默认的</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">obtain_auth_token</font>`<font style="color:rgb(92, 89, 98);">视图返回的json响应数据是非常简单的，只有token一项。如果你希望返回更多信息，比如用户id或email，就就要通过继承</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">ObtainAuthToken</font>`<font style="color:rgb(92, 89, 98);">类量身定制这个视图，如下所示：</font>

```python
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
```

<font style="color:rgb(92, 89, 98);">然后修改</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">urls.py</font>`<font style="color:rgb(92, 89, 98);">:</font>

```python
urlpatterns +=[
    path('api-token-auth/',CustomAuthToken.as_view())]
```

<font style="color:rgb(92, 89, 98);">最后一步，DRF的</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">TokenAuthentication</font>`<font style="color:rgb(92, 89, 98);">类会从请求头中获取Token，验证其有效性。如果token有效，返回</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">request.user</font>`<font style="color:rgb(92, 89, 98);">。至此，整个token的签发和验证就完成了。整个过程你清楚了吗?</font>

## <font style="color:rgb(39, 38, 43);">小结</font>
<font style="color:rgb(92, 89, 98);">本文总结了认证(authentication)的本质，DRF自带的几种认证方案及如何自定义认证方案。最后我们重点介绍了DRF中使用自带Token认证方案的整个流程。</font>

<font style="color:rgb(92, 89, 98);">JSON Web Token是一种更新的使用token进行身份认证的标准。与内置的TokenAuthentication方案不同，JWT身份验证不需要使用数据库来验证令牌, 而且可以轻松设置token失效期。Django中可以通过djangorestframework-simplejwt 这个第三方包轻松实现JWT认证，我们将在下篇文章中进行详细介绍。</font>

