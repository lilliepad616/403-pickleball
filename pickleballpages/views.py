from django.shortcuts import render
from pickleballpages.models import Court

# Create your views here.
from django.http import HttpResponse

def indexPageView(request) :
     return render(request, 'picklepagestemplates/index.html')

def aboutPageView(request) :
    return render(request, 'picklepagestemplates/about.html')

def equipPageView(request) :
    return render(request, 'picklepagestemplates/equipment.html')
    

def showCourtsPageView(request) :
    data = Court.objects.all()
    qs = Court.objects.all()
    court_query = request.GET.get('court')

    if court_query != '' and court_query is not None:
        qs = qs.filter(courtname__icontains = court_query)
    context = {
        "court" : data,
        'queryset' : qs
    }
    return render(request, 'picklepagestemplates/courts/courts.html', context)

def showSingleCourtPageView(request, court_id):
    data = Court.objects.get(id = court_id)

    context = {
        "record" : data,
    }
    return render(request, 'picklepagestemplates/courts/updatecourt.html', context)

def updateCourtPageView(request):
    if request.method == 'POST':
        court_id = request.POST['court_id']

        court = Court.objects.get(id=court_id)

        court.courtname = request.POST['courtname']
        court.courtaddress = request.POST['courtaddress']
        court.numberofcourts = request.POST['numberofcourts']
        court.courtofficiators = request.POST['courtofficiators']
        court.lights = request.POST['lights']
        court.closingtime = request.POST['closingtime']

        court.save()
    
    return showCourtsPageView(request)

def deleteCourtPageView(request, court_id):
    data = Court.objects.get(id=court_id)

    data.delete()

    return showCourtsPageView(request)

def addCourtPageView(request):
    if request.method == 'POST':
        court = Court()

        court.courtname = request.POST['courtname']
        court.courtaddress = request.POST['courtaddress']
        court.numberofcourts = request.POST['numberofcourts']
        court.courtofficiators = request.POST['courtofficiators']
        court.lights = request.POST['lights']
        court.closingtime = request.POST['closingtime']

        court.save()

        return showCourtsPageView(request)
    else:
        return render(request, 'picklepagestemplates/courts/createcourt.html')


# def courtSearchView(request):
#     qs = Court.objects.all()
#     court_query = request.GET.get('court')

#     if court_query != '' and court_query is not None:
#         qs = qs.filter(Name__icontains = court_query)

#     context = {
#         'queryset' : qs
#     }
#     return render(request, 'picklepagestemplates/courts/courts.html', context)