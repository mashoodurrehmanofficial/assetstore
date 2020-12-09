"""assets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls import include, url
from django.shortcuts import render,redirect
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

from root.sitemaps import *

sitemaps = {
    'article': Article_Sitemap(),
    'static': Static_Sitemap(),
}
def xml(request):
    return redirect('https://www.xml-sitemaps.com/download/unityfreepaidassets.com-a2d54aed8/sitemap.xml?view=1')

urlpatterns = [
    path('admin/admin/admin/naniwala/', admin.site.urls),  
    path('', include('root.urls')),     
    path('sitemap.xml',xml),
    # path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
     
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

