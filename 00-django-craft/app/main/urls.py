"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from django.conf.urls.static import static
from django.conf import settings

from tasks.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("index/<str:name>", index, name="index"),
    path("index/", index, name="index"),
    path("myform/", myform, name="myform"),
    path("create_task/", create_task, name="create_task"),

    # Cuidado con el orden de las rutas
    path("api/list_tasks/", list_tasks_api, name="list_tasks_api"),
    path("api/<str:name>/", api, name="api"),
    path("api/", api, name="api"),

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
