from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "variable1": "Harry is great",
        "variable2":"Akash is also great"
               }
    return render(request, 'index.html', context)
    # return HttpResponse("This is homepage")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is about page)

def services(request):
    return render(request, 'services.html')
    

def Clock(request):
    return render(request, 'JavaScript_Clock.html')

def To_Do_List(request):
    return render(request, 'To_Do_List.html')
    

def contact(request):
   if request.method == "POST":
     name = request.POST.get('name')
     email = request.POST.get('email')
     phone = request.POST.get('phone')
     desc = request.POST.get('desc')
     contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
     contact.save()
     messages.success(request, "Your message has been sent!")

   return render(request, 'contact.html')
    # return HttpResponse("This is conatct page")


