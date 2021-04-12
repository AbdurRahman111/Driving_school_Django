from django.shortcuts import render, redirect
from django.contrib import messages
from .models import contact_us

# Create your views here.


# about page
def about(request):
    return render(request, 'about.html')

# contact page
def contact(request):
    if request.method=="POST":
        # get email and message from template
        email=request.POST.get('email')
        msg=request.POST.get('msg')
        print(email, msg)

        # save contact us message to database
        contactus = contact_us(email=email, message=msg)
        contactus.save()
        messages.success(request, 'Message Has been sent to admin !!')
        return redirect('index')

    return render(request, 'contact.html')
