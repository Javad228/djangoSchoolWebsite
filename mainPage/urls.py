from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='mainPage-home'),
    path('student/<slug:stud_id>/attendance/', views.attendance, name='attendance'),
    path('about/', views.about, name='mainPage-about'),
    path('table/', views.table, name='table'),
]