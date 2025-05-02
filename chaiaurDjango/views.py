from django.http import HttpResponse
from django.shortcuts import render






def home(request):
    # return HttpResponse("Hello, world! This is the home page of the Django application from Chai aur Django.")
    return render(request, 'website/index.html')

def about(request):
    # return HttpResponse("Hello, world! This is the about page of the Django application from Chai aur Django.")
    return render(request, 'website/about.html')

def contact(request):
    # return HttpResponse("Hello, world! This is the contact page of the Django application from Chai aur Django.")
    return render(request, 'website/contact.html')