"""
URL configuration for telsko project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings


from . import views
urlpatterns = [
  
path('register/',views.register,name='register'),
path('login/',views.login,name='login'),
path('logout/',views.logout,name='logout'),
path('',views.users,name='users'),
path('search',views.search_flights,name='search_flights'),
path('book/', views.book_seat, name='book_seat'),
path('ticket/<int:flight_id>/<str:seat_number>/', views.ticket, name='ticket'),


]
