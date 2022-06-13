from django.contrib import admin

from users.models import *
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)
admin.site.register(Classes)
admin.site.register(Teaches)
admin.site.register(Instructor)
admin.site.register(Student)
admin.site.register(TeachesWithDate)
admin.site.register(Attendance)



# Register your models here.
