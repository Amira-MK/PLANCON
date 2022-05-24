"""plancon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from os import stat
from django.conf import settings
from django.urls import re_path
from django.contrib import admin
from django.urls import path, include
from authentication import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('addcon/',views.addcon,name="addcon"),
    path('addreview//<int:article_id>/<int:conf_id>/',views.addreview,name="addreview"),
    path('addarticle/<conf_id>/',views.addarticle,name="addarticle"), 
    path('', include('django.contrib.auth.urls')),
]
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
