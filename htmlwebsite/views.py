from django.http import HttpResponse
from django.shortcuts import render

from htmlwebsite.models import Contact , signin ,signup

# Create your views here.


def home(request):
    contactdata = Contact.objects.all()
    for a in contactdata:
        print(a.address)


    if request.method=='POST':
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        contact.name=name
        contact.email=email
        contact.phone=phone
        contact.address=address
        contact.save()
        return HttpResponse("Data Inserted Succesfully")
    # return HttpResponse("im website")
    return render(request,'page2.html')

def sigin(request):


    if request.method=='POST':
        Sin = signin()
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        Sin.username=username
        Sin.password=password
        Sin.save()
        return HttpResponse("Data Inserted Succesfully")
    return render(request,'signin.html')

def sigup(request):
    if request.method=='POST':
        Sup=signup()
        first_name = request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        username= request.POST.get('username')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        password= request.POST.get('password')

        Sup.first_name=first_name
        Sup.last_name=last_name
        Sup.username=username
        Sup.email=email
        Sup.phone=phone
        Sup.password=password
        Sup.save()
        return HttpResponse("Data Inserted Succesfully")
    return render(request,'signup.html')

def result(request):
    return render(request,'result.html')

def about(request):
    return render(request,'about.html')

def home1(request):
    return render(request,'home1.html')