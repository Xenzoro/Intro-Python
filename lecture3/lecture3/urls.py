"""
URL configuration for lecture3 project.

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
from django.urls import path
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls), #defult admin page
    path('', include("hello.urls")),
    path('hello/', include("hello.urls")), #this line tells Django to include the URL patterns defined in the hello app's urls.py file whenever a URL starts with "hello/". this allows us to organize our URL patterns in a modular way, keeping the URL configuration for the hello app separate from the main project URLs. when a user visits a URL that starts with "hello/", Django will look for matching patterns in the hello app's urls.py file and route the request accordingly.
    path('tasks/', include("tasks.urls")),
]
