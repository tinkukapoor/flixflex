"""demoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from demo import views
urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.home,name='home'),
    path('softwarecompanychandigarh/login/',views.login,name='login'),
    path('softwarecompanychandigarh/logout/',views.logout,name='logout'),
    #path('flixflex/auth',views.auth_view,name='auth_views'),
    path('softwarecompanychandigarh/loggedin/',views.login,name='login'),
    path('softwarecompanychandigarh/invalid/', views.invalid_login,name='invalid_login'),
    path('softwarecompanychandigarh/register/',views.register_user,name='register_user'),
    path('softwarecompanychandigarh/register_success/',views.register_success,name='register_success'),
    path('softwarecompanychandigarh/aboutus/',views.aboutus,name='aboutus'),
    path('softwarecompanychandigarh/cancel/',views.cancel,name='cancel'),
    path('softwarecompanychandigarh/services/',views.services,name='service'),
    path('softwarecompanychandigarh/informations/',views.information,name='information'),
]

