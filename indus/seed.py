from faker import Faker
import random
from .models import *

fake = Faker()

def seed_db(n=10) -> None:
    try:
        for _ in range(n):
            departments_objs=Department.objects.all()
            if departments_objs.exists():
                random_index=random.randint(0,len(departments_objs)-1)
                student_id=f'STUD-0{random.randint(100,999)}'
                department=departments_objs[random_index]
                student_name=fake.name()
                student_email=fake.email()
                student_age=random.randint(20,30)
                student_address=fake.address()

                student_id_objs=StudentId.objects.create(student_id=student_id)
                student_obj=Student.objects.create(
                    department=department,
                    student_id=student_id_objs,
                    student_name=student_name,
                    student_age=student_age,
                    student_email=student_email,
                    student_address=student_address
                )
    except Exception as e:
        print(f"An error occurred: {e}")

def create_student_marks() -> None:
    try:
        student_objs = Student.objects.all()
        for student in student_objs:
            subjects=Subject.objects.all()
            for subject in subjects:
                SubjectMarks.objects.create(
                    subject=subject,
                    student=student,
                    marks=random.randint(0,100)
                )
    except Exception as e:
        print(f'an error occurred in create_student_marks: {e}')