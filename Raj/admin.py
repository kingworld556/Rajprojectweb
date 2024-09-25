from django.contrib import admin
from Raj.models import *

# Register your models here.

class AdminStudent(admin.ModelAdmin):
    list_display=('Name','F_name','Age','Address','Email')

class AdminFees(admin.ModelAdmin):
    list_display=('name','fees')

admin.site.register(Fees,AdminFees)
admin.site.register(Student,AdminStudent)

