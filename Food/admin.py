from django.contrib import admin
from Food.models import *

# Register your models here.

class AdminRecipe(admin.ModelAdmin):
    list_display=('r_name','r_description','r_image')

admin.site.register(Recipe,AdminRecipe)