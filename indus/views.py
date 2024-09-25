from django.shortcuts import render, redirect
from django.db.models import *
from django.core.paginator import Paginator
from .models import *
# Create your views here.

def get_stud(request):
    search=request.GET.get('search','')
    queryset=Student.objects.all()

    if search:
        queryset = queryset.filter(
            Q(student_name__icontains=search) |
            Q(student_age__icontains=search) |
            Q(department__department__icontains=search) 
        )

    paginator=Paginator(queryset,10)
    page_number=request.GET.get('page',1)
    page_obj=paginator.get_page(page_number)

    return render(request,'stud/studs.html',{'queryset':page_obj})

def see_marks(request,student_id):
    queryset=SubjectMarks.objects.filter(student__student_id__student_id=student_id)
    totalmarks=queryset.aggregate(totalmarks = Sum('marks'))

    current_student_total=totalmarks['totalmarks']

    all_students_total_marks=SubjectMarks.objects.values('student').annotate(total_marks = Sum('marks')).order_by('-total_marks')

    rank = 1
    for student_marks in all_students_total_marks:
        if student_marks['total_marks'] > current_student_total:
            rank += 1

    return render(request,"stud/marks.html",{
                  "queryset" : queryset,
                  "totalmarks" : totalmarks,
                  "rank" : rank
                  })
