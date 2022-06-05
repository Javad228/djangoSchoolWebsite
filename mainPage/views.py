from django.contrib.auth.decorators import login_required
from django.http import request
from django.shortcuts import render, get_object_or_404
from django.core import serializers
from users.models import Account, Instructor, Classes, Student, Attendance

posts = [
    {
        'user': 'Javad',
        'title': 'Post',
        'content': 'Hello',
        'date_posted': '19/09'
    },
    {
        'user': 'Javid',
        'title': 'Post 2',
        'content': 'Hi',
        'date_posted': '20/09'
    }
]

@login_required(login_url='login/')
def home(request):
    if request.user.is_teacher:
        return render(request, 'mainPage/home_for_teach.html')
    else:
        return render(request, 'mainPage/home.html')


@login_required()
def about(request):
    return render(request, 'mainPage/about.html')

@login_required()
def table(request):
    system = request.POST.get('system',None)
    classes = Classes.objects.get(ClassChoice=system)
    context = {
        'system': classes.RegisteredStudents.all()
    }

    return render(request, 'mainPage/table.html', context)

@login_required()
def attendance(request, stud_id):
    student = get_object_or_404(Student, username=stud_id)
    att_list = Attendance.objects.filter(student=student).order_by('date')

    print(att_list.last().status)

    return render(request, 'mainPage/table.html', {'att_list': att_list})