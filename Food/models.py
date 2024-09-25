from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recipe(models.Model): 
    #user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    r_name=models.CharField(max_length=50)
    r_description=models.TextField()
    r_image=models.ImageField(upload_to="recipe_img")
    r_video = models.FileField(upload_to="recipe_videos", null=True, blank=True)  # For video upload

    def __str__(self):
        return self.r_name
