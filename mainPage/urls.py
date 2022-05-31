from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='mainPage-home'),
    path('about/', views.about, name='mainPage-about'),
    path('table/', views.table, name='table'),
]