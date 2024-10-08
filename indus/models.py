from django.db import models

# Create your models here.

class Department(models.Model):
    department=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.department
    
    class Meta:
        ordering=['department']

class StudentId(models.Model):
    student_id=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.student_id
    
class Student(models.Model):
    department=models.ForeignKey(Department,related_name="dept",on_delete=models.CASCADE,null=True,blank=True)
    student_id=models.OneToOneField(StudentId,related_name="studentid",on_delete=models.CASCADE,null=True,blank=True)
    student_name=models.CharField(max_length=50)
    student_email=models.EmailField(unique=True)
    student_age=models.IntegerField(default=18)
    student_address=models.TextField()

    def __str__(self) -> str:
        return self.student_name
    
    class Meta:
        ordering=['student_name']
        verbose_name="stud"

class Subject(models.Model):
    subject_name=models.CharField(max_length=100)

    def __str__(self) -> str :
        return self.subject_name
    
class SubjectMarks(models.Model):
    student=models.ForeignKey(Student,related_name="studentmarks",on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    marks=models.IntegerField()

    def __str__(self) -> str:
        return self.subject