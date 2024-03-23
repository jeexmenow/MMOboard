"""
URL configuration for fmmo project.

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
from ckeditor_uploader.views import upload, browse
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.decorators.cache import never_cache
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fan_forum.urls'), name='posts'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('sign/', include('sign.urls')),
    path('accounts/', include('allauth.urls')),
    re_path(r'^upload/', login_required(upload), name='ckeditor_upload'),
    re_path(r'^browse/', login_required(never_cache(browse)), name='ckeditor_browse'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)