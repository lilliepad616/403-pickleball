from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def indexPageView(request) :
    return HttpResponse('Hello Universe!')

def aboutPageView(request) :
    sOutput = '<html><head><title>My Title</title></head><body><p>Welcome to the about page</p></body></html>'
    return HttpResponse(sOutput)

def equipPageView(request) :
    sOutput = '<html><head><title>My Title</title></head><body><p>Welcome to the equipment page</p></body></html>'
    return HttpResponse(sOutput)

def courtsPageView(request) :
    sOutput = '<html><head><title>My Title</title></head><body><p>Welcome to the courts page</p></body></html>'
    return HttpResponse(sOutput) 