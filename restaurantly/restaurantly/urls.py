"""restaurantly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from djangofier import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('menu/', views.menu, name="menu"),
    path('specials/', views.specials, name="specials"),
    path('events/', views.events, name="events"),
    path('gallery/', views.gallery, name="gallery"),
    path('chefs/', views.chefs, name="chefs"),
    path('chef1/', views.chef1, name="chef1"),
    path('chef2/', views.chef2, name="chef2"),
    path('chef3/', views.chef3, name="chef3"),
    path('contact/', views.contact, name="contact"),
    path('book/', views.book, name="book"),
]
