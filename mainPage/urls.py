from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='mainPage-home'),
    path('teacher/<slug:teacher_id>/<int:choice>/Classes/', views.t_clas, name='t_clas'),
    path('teacher/<int:ass_id>/attendance/', views.attendance_t, name='attendance_t'),
    path('teacher/<int:ass_id>/edit_attendance/', views.t_edit_attendance, name='t_edit_attendance'),
    path('teacher/<slug:ass_id>/attendance/submit/', views.t_submit, name='submit_t'),
    path('student/<slug:stud_id>/attendance/', views.attendance, name='attendance'),
    path('about/', views.about, name='mainPage-about'),
    # path('teacher/<int:assign_id>/Extra_class/', views.attendance_t, name='attendance_t'),
    path('table/', views.table, name='table'),
]