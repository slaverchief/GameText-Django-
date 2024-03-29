"""
URL configuration for MagrasBox project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.template.defaulttags import url
from django.urls import path, include, re_path
from rest_framework import routers

from .sys_views import hand404
from . import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
    path('users/', include('authsys.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
    path('captcha/', include('captcha.urls')),
    path('roomchat/', include('chat.urls')),
    path('api/', include('rest_api.urls')),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) + \
                   static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = hand404
