from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def indexPageView(request) :
     return render(request, 'picklepagestemplates/index.html')

def aboutPageView(request) :
    return render(request, 'picklepagestemplates/about.html')

def equipPageView(request) :
    return render(request, 'picklepagestemplates/equipment.html')
    

def courtsPageView(request) :
     return render(request, 'picklepagestemplates/courts/courts.html')

def courtsCreatePageView(request) :
     return render(request, 'picklepagestemplates/courts/createcourt.html')

def courtsUpdatePageView(request) :
     return render(request, 'picklepagestemplates/courts/updatecourt.html')

def courtsDeletePageView(request) :
     return render(request, 'picklepagestemplates/courts/deletecourt.html')