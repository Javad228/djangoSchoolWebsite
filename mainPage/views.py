from django.shortcuts import render
from django.core import serializers
from users.models import Account, Instructor, Classes

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

def home(request):

    return render(request, 'mainPage/home.html')


def about(request):
    return render(request, 'mainPage/about.html')

def table(request):
    system = request.POST.get('system',None)
    classes = Classes.objects.get(ClassChoice=system)
    context = {
        'system': classes.RegisteredStudents.all()
    }

    return render(request, 'mainPage/table.html', context)


def attendance(request, stud_id):
    return render(request, 'mainPage/about.html')