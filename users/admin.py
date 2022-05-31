from django.contrib import admin

from users.forms import UserRegisterForm
from users.models import Account, Classes, Attends, Instructor


class CarAdmin(admin.ModelAdmin):
    form = UserRegisterForm

admin.site.register(Account, CarAdmin)
admin.site.register(Classes)
admin.site.register(Attends)
admin.site.register(Instructor)
# Register your models here.
