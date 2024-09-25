from django.shortcuts import render

# Create your views here.

def userget(request):
    ans = 0
    try:
        if request.method=="GET":
            n1=int(request.GET.get('num1',0))
            n2=int(request.GET.get('num2',0))
            ans=n1+n2
    except:
        pass
    return render(request,"student/getmethod.html",{"ans":ans}) 

def userpost(request):
    ans = 0
    data = {
        'n1':0,
        'n2':0,
        'ans':ans
    }
    try:
        if request.method=="POST":
            n1=int(request.POST.get('num1',0))
            n2=int(request.POST.get('num2',0))
            ans=n1+n2
            data = {
                'n1':n1,
                'n2':n2,
                'ans':ans
            }
    except:
        pass
    return render(request,"student/postmethod.html",{"ans":ans}) 


def calculator(request):
    result=''
    if request.method == "POST":
        try:
            n1 = int(request.POST.get('n1'))
            n2 = int(request.POST.get('n2'))
            opr  = request.POST.get('opr')
            if opr == "+":
                result = n1 + n2
            elif opr == "-":
                result = n1 - n2
            elif opr == "*":
                result = n1 * n2
            elif opr == "/":
                result = n1 / n2
            else:
                result = "Invalid Operation"
        except:
            pass
    return render(request,"student/calculator.html",{'result':result})

def even_odd(request):
    result = ""
    if request.method == "POST":
        try:
            n1 = int(request.POST.get('n1'))
            if n1 % 2 == 0:
                result = "Even"
            else:
                result = "Odd"
        except:
            pass
    return render(request,"student/even.html",{"result":result})

def cal_marks(request):
    tot= 0
    per= 0
    grade= ""
    marks = []

    if request.method == "POST":
        try:
            # Collect marks from POST data
            for i in range(1, 6):
                mark = int(request.POST.get(f'subject{i}', 0))
                marks.append(mark)

            # Calculate total and percentage
            tot =int( sum(marks))
            per = int((tot / 500) * 100)

            # Determine grade
            if per >= 90:
                grade = 'A'
            elif per >= 80:
                grade = 'B'
            elif per >= 75:
                grade = 'C'
            elif per >= 65:
                grade = 'D'
            else:
                grade = 'E'

        except ValueError:
            pass

    return render(request, 'student/result.html', {'tot': tot, 'per': per, 'grade': grade} )

def mark(request):
    return render(request,"marks.html")
 