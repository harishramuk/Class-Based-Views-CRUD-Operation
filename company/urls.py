"""company URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from TestApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.companylistview.as_view(),name='company'),
    path('<int:pk>/',views.companydetailview.as_view(),name='detail'),
    path('create/',views.companycreateview.as_view()),
    path('update/<int:pk>',views.companyupdateview.as_view()),
    path('delete/<int:pk>',views.companydeleteview.as_view()),

]
