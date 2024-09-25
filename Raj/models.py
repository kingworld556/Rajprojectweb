from django.db import models

# Create your models here.

class Student(models.Model):
    Name=models.CharField(max_length=20)
    F_name=models.CharField(max_length=20)
    Age=models.IntegerField()
    Address=models.TextField()
    Email=models.EmailField()

class Fees(models.Model):
    name=models.CharField(max_length=20)
    fees=models.IntegerField()

    def __str__(self)->str:
        return f"{self.name} {self.fees}"

