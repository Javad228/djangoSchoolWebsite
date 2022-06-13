from django.contrib.auth.decorators import login_required
from django.http import request
from django.shortcuts import render, get_object_or_404
from django.core import serializers
from users.models import User, Instructor, Classes, Student, Attendance, TeachesWithDate, Teaches

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
    acc = User.objects.get(username=request.user.username)
    print(acc.is_student)
    if acc.is_student:
        return render(request, 'mainPage/home.html')
    else:
        return render(request, 'mainPage/home_for_teach.html')


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

    # print(att_list.last().status)

    return render(request, 'mainPage/table.html', {'att_list': att_list})


def attendance_t(request, ass_id):
    ass = get_object_or_404(Teaches, id=ass_id)
    classes_taught = ass.classes
    context = {
        'ass': ass,
        'classes_taught': classes_taught,
    }
    print(ass)
    # for s in classes_taught.student_set.all():
    #     print(s)
    # print(classes_taught.student_set.all())
    return render(request, 'mainPage/teacher_attendance_new_class.html',context)


def t_clas(request, teacher_id, choice):
    print(teacher_id)
    person = get_object_or_404(User, username=teacher_id)
    teacher = get_object_or_404(Instructor, user=person)
    return render(request, 'mainPage/class_choice.html', {'teacher': teacher,
                                                          'choice': choice
                                                          })


def t_submit(request, ass_id):
    ass = get_object_or_404(Teaches, id=ass_id)
    cl = ass.classes
    cr = ass.classes_id
    assc = ass.teacheswithdate_set.create(latenessStatus=1, date=request.POST['date'])
    assc.save()

    for i, s in enumerate(cl.student_set.all()):
        status = request.POST[s.username]
        if status == 'present':
            status = 0
        elif status == 'absent':
            status = 1
        else:
            status = 2
        date = request.POST['date']
        a = Attendance(course=cl, student=s, status=status, date=date, attendanceclass=assc)
        a.save()


    return render(request, 'mainPage/about.html')


def t_edit_attendance(request, ass_id):
    print(ass_id)
    return render(request, 'mainPage/about.html')