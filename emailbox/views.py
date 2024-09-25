from django.shortcuts import render , redirect
from django.core.mail import send_mail
from .forms import Emailform

# Create your views here.

def send_email(request):
    if request.method == 'POST':
        form = Emailform(request.POST)
        if form. is_valid():
            subject=form.cleaned_data['subject']
            message=form.cleaned_data['message']
            recipient=form.cleaned_data['recipient']

            send_mail(
                subject,
                message,
                'your_email@gmail.com',
                [recipient]
            )
            return render(request,'box/email.html')
        
    else:
        form = Emailform()

    return render(request,'box/send_email.html',{'form':form})
