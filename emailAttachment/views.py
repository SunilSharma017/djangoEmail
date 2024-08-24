from django.http import HttpResponse
from django.shortcuts import render,redirect
from tcaemail.models import workData
from django.core.mail import EmailMessage,send_mail


def Home(request):
    if request.method=="POST":
        name=request.POST.get("n1")
        email=request.POST.get("n2")
        file=request.FILES.get("n3")
        print(file)
        workData.objects.create(name=name,email=email)
    
        subject="djanog files attachment"
        message=f""" hey {name} 
         rthis mail is regarding your job . 
          we are sending our job descripiton here  """
        from_email="sharmasunil7742@gmail.com"
        recipient_list=[email]
        mail=EmailMessage(subject,message,from_email,recipient_list)
        mail.attach_file("Screenshot (92).png")
        mail.attach(file.name,file.read(),file.content_type)
        mail.send()
    return render(request,"index.html")