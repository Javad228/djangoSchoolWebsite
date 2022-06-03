from datetime import date

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser

import users


class Account(AbstractUser):
    @property
    def is_student(self):
        if hasattr(self, 'student'):
            return True
        return False

    @property
    def is_teacher(self):
        if hasattr(self, 'teacher'):
            return True
        return False


class Classes(models.Model):
    id = models.CharField(primary_key='True', max_length=50)

    class Meta:
        verbose_name_plural = 'classes'

    def __str__(self):
        return self.id


class Student(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, null=True)
    fullName = models.CharField(max_length=200)
    class_id = models.ForeignKey(Classes, on_delete=models.CASCADE, default=1)
    username = models.CharField(primary_key='True', max_length=100)

    def __str__(self):
        return self.fullName


class Instructor(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, null=True)
    fullName = models.CharField(max_length=200)
    username = models.CharField(primary_key='True', max_length=100)

    def __str__(self):
        return self.fullName


class Teaches(models.Model):
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE)
    taughtBy = models.ForeignKey(Instructor, on_delete=models.CASCADE)

    def __str__(self):
        classesIn = Classes.objects.get(id=self.classes_id)
        teachersIn = Instructor.objects.get(username=self.taughtBy_id)
        return '%s : %s' % (classesIn.id, teachersIn.username)

class TeachesWithDate(models.Model):
    assign = models.ForeignKey(Teaches, on_delete=models.CASCADE)
    date = models.DateField()
    latenessStatus = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Attendance'
        verbose_name_plural = 'Attendance'


class Attendance(models.Model):
    course = models.ForeignKey(Classes, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    attendanceclass = models.ForeignKey(TeachesWithDate, on_delete=models.CASCADE, default=1)
    date = models.DateField(default='2018-10-23')
    status = models.BooleanField(default='True')

    def __str__(self):
        sname = Student.objects.get(name=self.student)
        cname = Classes.objects.get(name=self.course)
        return '%s : %s' % (sname.fullName, cname.id)
