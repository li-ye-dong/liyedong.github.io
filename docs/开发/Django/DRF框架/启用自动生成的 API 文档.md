在 Django REST framework（DRF） 中启用自动生成的 API 文档（即 Swagger / Redoc 文档界面），**官方推荐的方式是使用 **`**drf-spectacular**`** 或 **`**drf-yasg**`。

---

我推荐你使用功能更全、更现代的 📘 **drf-spectacular**，下面我会详细说明两种方式。

---

## ✅ 方式一：使用 [drf-spectacular](https://github.com/tfranzel/drf-spectacular)（官方推荐）
### 🔧 第一步：安装依赖
```bash
pip install drf-spectacular
```

---

### 🛠 第二步：配置 Django 设置
在你的 `settings.py` 中添加：

```python
INSTALLED_APPS = [
    ...
    'drf_spectacular',
]

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}
```

---

### 🌐 第三步：配置 URL 路由（`urls.py`）
```python
from django.contrib import admin
from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # OpenAPI schema 文件（JSON）
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    # Swagger UI 页面
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # Redoc 页面
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
```

---

### ✅ 成功后效果：
+ 访问 `http://127.0.0.1:8000/api/docs/` → Swagger UI 文档；
+ 访问 `http://127.0.0.1:8000/api/redoc/` → Redoc 文档；
+ 访问 `http://127.0.0.1:8000/api/schema/` → OpenAPI JSON schema。

---

## ✅ 方式二：使用 [drf-yasg](https://github.com/axnsan12/drf-yasg)（老牌但好用）
### 安装：
```bash
pip install drf-yasg
```

### URL 配置（简版）：
```python
from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="你的 API 标题",
      default_version='v1',
      description="API 文档描述",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Swagger
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
```

---

## 🚀 总结推荐
| 需求 | 推荐 |
| --- | --- |
| 想用现代 OpenAPI3.0 标准、官方推荐 | ✅ `drf-spectacular` |
| 想快速集成、兼容老项目 | ✅ `drf-yasg` |


如果你愿意，我可以根据你的项目结构生成完整配置文件模板（包括 views 和 serializers 示例）。需要的话告诉我即可。

