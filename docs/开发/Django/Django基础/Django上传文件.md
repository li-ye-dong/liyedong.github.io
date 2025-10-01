## <font style="color:rgb(39, 38, 43);">Django文件上传需要考虑的重要事项</font>
<font style="color:rgb(92, 89, 98);">文件或图片一般通过表单进行。用户在前端点击文件上传，然后以POST方式将数据和文件提交到服务器。服务器在接收到POST请求后需要将其存储在服务器上的某个地方。Django默认的存储地址是相对于根目录的/media/文件夹，存储的默认文件名就是文件本来的名字。上传的文件如果不大于2.5MB，会先存入服务器内存中，然后再写入磁盘。如果上传的文件很大，Django会把文件先存入临时文件，再写入磁盘。</font>

<font style="color:rgb(92, 89, 98);">Django默认处理方式会出现一个问题，所有文件都存储在一个文件夹里。不同用户上传的有相同名字的文件可能会相互覆盖。另外用户还可能上传一些不安全的文件如js和exe文件，我们必需对允许上传文件的类型进行限制。因此我们在利用Django处理文件上传时必需考虑如下3个因素:</font>

+ <font style="color:rgb(92, 89, 98);">设置存储上传文件的文件夹地址</font>
+ <font style="color:rgb(92, 89, 98);">对上传文件进行重命名</font>
+ <font style="color:rgb(92, 89, 98);">对可接受的文件类型进行限制(表单验证)</font>

<font style="color:rgb(92, 89, 98);">注意：以上事项对于上传图片是同样适用的。</font>

## <font style="color:rgb(39, 38, 43);">Django文件上传的3种常见方式</font>
<font style="color:rgb(92, 89, 98);">Django文件上传一般有3种方式(如下所示)。我们会针对3种方式分别提供代码示范。</font>

+ <font style="color:rgb(92, 89, 98);">使用一般的自定义表单上传，在视图中手动编写代码处理上传的文件</font>
+ <font style="color:rgb(92, 89, 98);">使用由模型创建的表单(ModelForm)上传，使用</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">form.save()</font>`<font style="color:rgb(92, 89, 98);">方法自动存储</font>
+ <font style="color:rgb(92, 89, 98);">使用Ajax实现文件异步上传，上传页面无需刷新即可显示新上传的文件</font>

<font style="color:rgb(92, 89, 98);">Ajax文件上传部分见Django与Ajax交互篇。</font>

## <font style="color:rgb(39, 38, 43);">项目创建与设置</font>
<font style="color:rgb(92, 89, 98);">我们先使用</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">django-admin startproject</font>`<font style="color:rgb(92, 89, 98);">命令创建一个叫</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">file_project</font>`<font style="color:rgb(92, 89, 98);">的项目，然后cd进入</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">file_project</font>`<font style="color:rgb(92, 89, 98);">, 使用</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">python manage.py startapp</font>`<font style="color:rgb(92, 89, 98);">创建一个叫</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">file_upload</font>`<font style="color:rgb(92, 89, 98);">的app。</font>

<font style="color:rgb(92, 89, 98);">我们首先需要将</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">file_upload</font>`<font style="color:rgb(92, 89, 98);">这个app加入到我们项目里，然后设置/media/和/STATIC_URL/文件夹。我们上传的文件都会放在/media/文件夹里。我们还需要使用css和js这些静态文件，所以需要设置STATIC_URL。</font>

```python
#file_project/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'file_upload',# 新增
]

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static"), ]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

#file_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('file/', include("file_upload.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## <font style="color:rgb(39, 38, 43);">创建模型</font>
<font style="color:rgb(92, 89, 98);">使用Django上传文件创建模型不是必需，然而如果我们需要对上传文件进行系统化管理，模型还是很重要的。我们的File模型包括</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">file</font>`<font style="color:rgb(92, 89, 98);">和</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">upload_method</font>`<font style="color:rgb(92, 89, 98);">两个字段。我们通过</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">upload_to</font>`<font style="color:rgb(92, 89, 98);">选项指定了文件上传后存储的地址，并对上传的文件名进行了重命名。</font>

```python
#file_upload/models.py
from django.db import models
import os
import uuid

# Create your models here.
# Define user directory path
def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    return os.path.join("files", filename)

class File(models.Model):
    file = models.FileField(upload_to=user_directory_path, null=True)
    upload_method = models.CharField(max_length=20, verbose_name="Upload Method")
```

<font style="color:rgb(92, 89, 98);">注意：如果你不使用</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">ModelForm</font>`<font style="color:rgb(92, 89, 98);">，你还需要手动编写代码存储上传文件。</font>

## <font style="color:rgb(39, 38, 43);">URLConf配置</font>
<font style="color:rgb(92, 89, 98);">本项目一共包括3个urls, 分别对应普通表单上传，ModelForm上传和显示文件清单。</font>

```python
#file_upload/urls.py
from django.urls import re_path, path
from . import views

# namespace
app_name = "file_upload"

urlpatterns = [
    # Upload File Without Using Model Form
    re_path(r'^upload1/$', views.file_upload, name='file_upload'),

    # Upload Files Using Model Form
    re_path(r'^upload2/$', views.model_form_upload, name='model_form_upload'),

    # View File List
    path('file/', views.file_list, name='file_list'),

]
```

## <font style="color:rgb(39, 38, 43);">使用一般表单上传文件</font>
<font style="color:rgb(92, 89, 98);">我们先定义一个一般表单</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">FileUploadForm</font>`<font style="color:rgb(92, 89, 98);">，并通过clean方法对用户上传的文件进行验证，如果上传的文件名不以jpg, pdf或xlsx结尾，将显示表单验证错误信息。关于表单的自定义和验证更多内容见Django基础: 表单forms的设计与使用。</font>

```python
#file_upload/forms.py

from django import forms
from .models import File

# Regular form
class FileUploadForm(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    upload_method = forms.CharField(label="Upload Method", max_length=20,
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))
    def clean_file(self):
        file = self.cleaned_data['file']
        ext = file.name.split('.')[-1].lower()
        if ext not in ["jpg", "pdf", "xlsx"]:
            raise forms.ValidationError("Only jpg, pdf and xlsx files are allowed.")
        # return cleaned data is very important.
        return file
```

<font style="color:rgb(92, 89, 98);">注意： 使用clean方法对表单字段进行验证时，别忘了return验证过的数据，即</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">cleaned_data</font>`<font style="color:rgb(92, 89, 98);">。只有返回了cleaned_data, 视图中才可以使用form.cleaned_data.get(‘xxx’)获取验证过的数据。</font>

<font style="color:rgb(92, 89, 98);">对应一般文件上传的视图</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">file_upload</font>`<font style="color:rgb(92, 89, 98);">方法如下所示。当用户的请求方法为POST时，我们通过</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">form.cleaned_data.get('file')</font>`<font style="color:rgb(92, 89, 98);">获取通过验证的文件，并调用自定义的</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">handle_uploaded_file</font>`<font style="color:rgb(92, 89, 98);">方法来对文件进行重命名，写入文件。如果用户的请求方法不为POST，则渲染一个空的</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">FileUploadForm</font>`<font style="color:rgb(92, 89, 98);">在</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">upload_form.html</font>`<font style="color:rgb(92, 89, 98);">里。我们还定义了一个</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">file_list</font>`<font style="color:rgb(92, 89, 98);">方法来显示文件清单。</font>

```python
#file_upload/views.py

from django.shortcuts import render, redirect
from .models import File
from .forms import FileUploadForm, FileUploadModelForm
import os
import uuid
from django.http import JsonResponse
from django.template.defaultfilters import filesizeformat

# Create your views here.


# Show file list
def file_list(request):
    files = File.objects.all().order_by("-id")
    return render(request, 'file_upload/file_list.html', {'files': files})

# Regular file upload without using ModelForm
def file_upload(request):
    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # get cleaned data
            upload_method = form.cleaned_data.get("upload_method")
            raw_file = form.cleaned_data.get("file")
            new_file = File()
            new_file.file = handle_uploaded_file(raw_file)
            new_file.upload_method = upload_method
            new_file.save()
            return redirect("/file/")
    else:
        form = FileUploadForm()

    return render(request, 'file_upload/upload_form.html', 
                  {'form': form, 'heading': 'Upload files with Regular Form'}
                 )

def handle_uploaded_file(file):
    ext = file.name.split('.')[-1]
    file_name = '{}.{}'.format(uuid.uuid4().hex[:10], ext)

    # file path relative to 'media' folder
    file_path = os.path.join('files', file_name)
    absolute_file_path = os.path.join('media', 'files', file_name)

    directory = os.path.dirname(absolute_file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(absolute_file_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    return file_path
```

<font style="color:rgb(92, 89, 98);">注意：</font>

+ `<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">handle_uploaded_file</font>`<font style="color:rgb(92, 89, 98);">方法里文件写入地址必需是包含</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">/media</font>`<font style="color:rgb(92, 89, 98);">/的绝对路径，如果/media/files/xxxx.jpg，而该方法返回的地址是相对于/media/文件夹的地址，如/files/xxx.jpg。存在数据中字段的是相对地址，而不是绝对地址。</font>
+ <font style="color:rgb(92, 89, 98);">构建文件写入绝对路径时请用</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">os.path.join</font>`<font style="color:rgb(92, 89, 98);">方法，因为不同系统文件夹分隔符不一样。写入文件前一个良好的习惯是使用</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">os.path.exists</font>`<font style="color:rgb(92, 89, 98);">检查目标文件夹是否存在，如果不存在先创建文件夹，再写入。</font>

<font style="color:rgb(92, 89, 98);">上传表单模板</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">upload_form.html</font>`<font style="color:rgb(92, 89, 98);">代码如下:</font>

```python
#file_upload/templates/upload_form.html
{% extends "file_upload/base.html" %}
{% block content %}
{% if heading %}
<h3>{{ heading }}</h3>
{% endif %}

 <form action="" method="post" enctype="multipart/form-data" >
{% csrf_token %}
{{ form.as_p }}
<button class="btn btn-info form-control " type="submit" value="submit">Upload</button>
</form>
{% endblock %}
```

<font style="color:rgb(92, 89, 98);">显示文件清单模板</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">file_list.html</font>`<font style="color:rgb(92, 89, 98);">代码如下所示:</font>

```python
# file_upload/templates/file_list.html
{% extends "file_upload/base.html" %}

{% block content %}
<h3>File List</h3>
<p> <a href="/file/upload1/">RegularFormUpload</a> | <a href="/file/upload2/">ModelFormUpload</a>
| <a href="/file/upload3/">AjaxUpload</a></p>
{% if files %}
<table class="table table-striped">
<tbody>
<tr>
<td>Filename & URL</td>
<td>Filesize</td>
<td>Upload Method</td>
</tr>
{% for file in files %}
<tr>
<td><a href="{{ file.file.url }}">{{ file.file.url }}</a></td>
<td>{{ file.file.size | filesizeformat }}</td>
<td>{{ file.upload_method }}</td>
</tr>
{% endfor %}
</tbody>
</table>

{% else %}

<p>No files uploaded yet. Please click <a href="{% url 'file_upload:file_upload' %}">here</a>
to upload files.</p>
{% endif %}
{% endblock %}
```

<font style="color:rgb(92, 89, 98);">注意： </font>

+ <font style="color:rgb(92, 89, 98);">对于上传的文件我们可以调用</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">file.url</font>`<font style="color:rgb(92, 89, 98);">,</font><font style="color:rgb(92, 89, 98);"> </font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">file.name</font>`<font style="color:rgb(92, 89, 98);">和</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">file.size</font>`<font style="color:rgb(92, 89, 98);">来查看上传文件的链接，地址和大小。</font>
+ <font style="color:rgb(92, 89, 98);">上传文件的大小默认是以B显示的，数字非常大。使用Django模板过滤器</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">filesizeformat</font>`<font style="color:rgb(92, 89, 98);">可以将文件大小显示为人们可读的方式，如MB，KB。</font>

## <font style="color:rgb(39, 38, 43);">使用ModelForm上传文件</font>
<font style="color:rgb(92, 89, 98);">使用</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">ModelForm</font>`<font style="color:rgb(92, 89, 98);">上传是小编我推荐的上传方式，前提是你已经在模型中通过</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">upload_to</font>`<font style="color:rgb(92, 89, 98);">选项自定义了用户上传文件存储地址，并对文件进行了重命名。我们首先要自定义自己的</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">FileUploadModelForm</font>`<font style="color:rgb(92, 89, 98);">，由File模型重建的。代码如下所示:</font>

```python
#file_upload/forms.py
from django import forms
from .models import File

# Model form
class FileUploadModelForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('file', 'upload_method',)
        widgets = {
            'upload_method': forms.TextInput(attrs={'class': 'form-control'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def clean_file(self):
        file = self.cleaned_data['file']
        ext = file.name.split('.')[-1].lower()
        if ext not in ["jpg", "pdf", "xlsx"]:
            raise forms.ValidationError("Only jpg, pdf and xlsx files are allowed.")
        # return cleaned data is very important.
        return file
```

<font style="color:rgb(92, 89, 98);">使用</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">ModelForm</font>`<font style="color:rgb(92, 89, 98);">处理文件上传的视图</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">model_form_upload</font>`<font style="color:rgb(92, 89, 98);">方法非常简单，只需调用</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">form.save()</font>`<font style="color:rgb(92, 89, 98);">即可，无需再手动编写代码写入文件。</font>

```python
#file_upload/views.py

from django.shortcuts import render, redirect
from .models import File
from .forms import FileUploadForm, FileUploadModelForm
import os
import uuid
from django.http import JsonResponse
from django.template.defaultfilters import filesizeformat

# Create your views here.
# Upload File with ModelForm

def model_form_upload(request):
    if request.method == "POST":
        form = FileUploadModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() # 一句话足以
            return redirect("/file/")
    else:
        form = FileUploadModelForm()

    return render(request, 'file_upload/upload_form.html', 
                  {'form': form,'heading': 'Upload files with ModelForm'}
                 )
```

<font style="color:rgb(92, 89, 98);">模板跟前面一样，这里就不展示了。</font>

## <font style="color:rgb(39, 38, 43);">Django Ajax案例2：Ajax上传文件</font>
<font style="color:rgb(92, 89, 98);">前端模板及js文件如下所示, 请注意我们是如何在表单中加入了</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">enctype</font>`<font style="color:rgb(92, 89, 98);">属性，如何使用</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">FormData</font>`<font style="color:rgb(92, 89, 98);">上传文件，并解决了</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">csrftoken</font>`<font style="color:rgb(92, 89, 98);">问题的。</font>

```python
{% block content %}
<form action="" method="post" enctype="multipart/form-data" id="form">
<ul class="errorlist"></ul>
{% csrf_token %}
{{ form.as_p }}
<input type="button" class="btn btn-info form-control" value="submit" id="btn" />
</form>
<table class="table table-striped" id="result">
</table>
{% endblock %}

{% block js %}
    <script src=" https://cdn.jsdelivr.net/jquery.cookie/1.4.1/jquery.cookie.min.js ">
               </script>
               <script>
               var csrftoken = $.cookie('csrftoken');
function csrfSafeMethod(method) {
return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$(document).ready(function(){
                  $('#btn').click(function(e){
                      e.preventDefault();
                      // 构建FormData对象
                      var form_data = new FormData();
                         form_data.append('file', $('#id_file').files[0]);
                         $.ajax({
                          url: '/file/ajax_upload/',
                          data: form_data,
                          type: 'POST',
                          dataType: 'json',
                          // 告诉jQuery不要去处理发送的数据, 发送对象。
                                processData : false,
                                // 告诉jQuery不要去设置Content-Type请求头
                      contentType : false,
                      // 获取POST所需的csrftoken
                      beforeSend: function(xhr, settings) {
                      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                          xhr.setRequestHeader("X-CSRFToken", csrftoken);
                      }},
                          success: function (data) {
                      if(data['error_msg']) {
                          var content = '<li>'+ data['error_msg'] + '</li>';
                                     $('ul.errorlist').html(content);
                      }
                          else
                      {
                          var content= '<thead><tr>' +
                                     '<th>Name and URL</th>' +
                                     '<th>Size</th>' +
                                     '</tr></thead><tbody>';
                                     $.each(data, function(i, item) {
                                            content = content +
                                                   '<tr><td>' +
                                                   "<a href= ' " +
                                                   item['url'] +
                                                   " '> " +
                                                   item['url'] +
                                                   '</a></td><td>' +
                                                   item['size'] +
                                                   '</td><td><tr>'
                                                   });
                                            content = content + "</tbody>";
                                            $('#result').html(content);
                      }
                      },
                      });
                                  });
                  });
</script>
{% endblock %}
```

<font style="color:rgb(92, 89, 98);">Django负责处理视图Ajax请求的视图函数如下所示：</font>

```python
# handling AJAX requests
def ajax_upload(request):
    if request.method == "POST":
        form = FileUploadModelForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            # Obtain the latest file list
            files = File.objects.all().order_by('-id')
            data = []
            for file in files:
                data.append({
                    "url": file.file.url,
                    "size": filesizeformat(file.file.size),
                })
            return JsonResponse(data, safe=False)
        else:
            data = {'error_msg': "Only jpg, pdf and xlsx files are allowed."}
            return JsonResponse(data)
    return JsonResponse({'error_msg': 'only POST method accpeted.'})
```

