from datetime import date

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

import users


class MyAccountManager(BaseUserManager):

    def create_user(self, email, username, first_name, last_name, typeOf, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            typeOf=typeOf,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, typeOf, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            first_name=first_name,
            last_name=last_name,
            typeOf=typeOf,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



class Account(AbstractBaseUser, models.Model):
    username = models.CharField(verbose_name="username", max_length=30, unique=True)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # ClassChoice = models.ManyToManyField(Classes)
    student = 'PT'
    parent = 'ST'
    curator = 'CR'
    type_of_user = [
        (student, 'student'),
        (parent, 'parent'),
        (curator, 'curator'),
    ]
    typeOf = models.CharField(max_length=2,
                              choices=type_of_user,
                              default=student)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'typeOf']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

        # For checking permissions. to keep it simple all admin have ALL permissons

    def has_perm(self, perm, obj=None):
        return self.is_admin

        # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)

    def has_module_perms(self, app_label):
        return True

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








