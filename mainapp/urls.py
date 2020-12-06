"""Licenses URL Configuration

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
import mainapp.views as mainapp
from django.urls import path
from mainapp.views import LicenseView

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='main'),
    path('create/', mainapp.bulk_creation_view, name='create'),
    path('update/', mainapp.update, name='update'),
    path('api/license/', LicenseView.as_view(), name='api'),
]
