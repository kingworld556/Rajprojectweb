from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    p=[
        {'name':'nisha','age':15},
        {'name':'rathee','age':25},
        {'name':'arjun','age':17},
        {'name':'prabhu','age':25},
        {'name':'aakash','age':15},
        {'name':'deepak','age':35},
        {'name':'Ankit','age':18},
        {'name':'Ayush','age':16},
        {'name':'deepika','age':21},   
    ]
    return render(request,"studio\index.html",context={'p':p}) 

def page(request):
    return HttpResponse("success")

def contact(request):
    return render(request,"studio/contact.html")

def about(request):
    return render(request,"studio/about.html")