from django.contrib import admin

from users.models import Account, Classes, Attends, Instructor


admin.site.register(Account)
admin.site.register(Classes)
admin.site.register(Attends)
admin.site.register(Instructor)
# Register your models here.
