from django.contrib import admin

from users.models import *


admin.site.register(Account)
admin.site.register(Classes)
admin.site.register(Teaches)
admin.site.register(Instructor)
admin.site.register(Student)
admin.site.register(TeachesWithDate)
admin.site.register(Attendance)



# Register your models here.
