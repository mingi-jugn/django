from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('write/', views.write, name='write'),
    path('login/', views.login, name='login'),
    path('question/', views.question, name='question'),
    path('bulletin/', views.bulletin, name='bulletin'),
    path("detail/<int:pk>/", views.detail, name="detail"),
    path("join/", views.join, name="join"),
    path("logout/", views.logout, name="logout"),
    path("error/", views.error, name="error"),
    path("list/", views.list, name="list"),
    path("getlist/<getuser>", views.getlist, name="getlist"),

]