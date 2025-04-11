"""
URL configuration for django_learn_it_all project.

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
from django.urls import path, include
from basic_learn import urls
from student import urls
from api import urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("basic/", include("basic_learn.urls")),
    # web application endpoints
    path("students/", include("student.urls")),
    # API End points
    path("api/v1/", include("api.urls"))
]
