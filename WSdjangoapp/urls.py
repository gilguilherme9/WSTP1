"""WSdjangoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app.views import indexpage, sendinfo, addtriple, rmtriple, downloadgraphvis, inferenciarisco,inferenciarelacao,inferenciainfeliz

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^downloadgraphvis',downloadgraphvis,name='downloadgraphvis'),
    url(r'^index/',indexpage,name='index'),
    url(r'^sendinfo',sendinfo,name='sendinfo'),
    url(r'^addtriple',addtriple,name='addtriple'),
    url(r'^rmtriple',rmtriple,name='rmtriple'),
    url(r'^inferenciarisco', inferenciarisco, name='inferenciarisco'),
    url(r'^inferenciainfeliz', inferenciainfeliz, name='inferenciainfeliz'),
    url(r'^inferenciarelacao', inferenciarelacao, name='inferenciarelacao')

]
