from django.contrib import admin
from .models import *

# Register your models here.
class SubjectMarksAdmin(admin.ModelAdmin):
    list_display=['student','subject','marks']

admin.site.register(Department)
admin.site.register(StudentId)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(SubjectMarks,SubjectMarksAdmin)