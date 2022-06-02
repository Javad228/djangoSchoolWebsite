from datetime import date

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser

import users



class Account(AbstractUser):
    @property
    def is_parent(self):
        if hasattr(self, 'parent'):
            return True
        return False

    @property
    def is_teacher(self):
        if hasattr(self, 'teacher'):
            return True
        return False

class Classes(models.Model):
    CLASS_CHOICES = (
        ('PH', 'Physics'),
        ('CH', 'Chemistry'),
        ('MA', 'Math'),
        ('JA', 'Java'),
        ('PY', 'Python'),
    )

    ClassChoice = models.CharField(max_length=20, choices=CLASS_CHOICES, unique=True)
    RegisteredStudents = models.ManyToManyField(Account)



    def __str__(self):
        return self.ClassChoice

class Instructor(models.Model):
    name = models.CharField(max_length=30)
    classTaught = models.ManyToManyField(Classes)

class Attends(models.Model):
    students = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    classes = models.ForeignKey(Classes, on_delete=models.DO_NOTHING)
    taughtBy = models.ForeignKey(Instructor, on_delete=models.DO_NOTHING, default=1)
    isAbsent = models.BooleanField(default=False)
    isLate = models.BooleanField(default=False)
    dateAndTime = models.DateField(primary_key=True,verbose_name='Session date', default=date.today)








