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

# def showCustomersPageView(request) :
#     data = Customer.objects.all()

#     context = {
#         "cust" : data
#     }
#     return render(request, 'homepages/showCustomers.html', context)

# def showSingleCustomerPageView(request, cust_id):
#     data = Customer.objects.get(id = cust_id)

#     context = {
#         "record" : data,
#     }
#     return render(request, 'homepages/editCustomer.html', context)

# def updateCustomerPageView(request):
#     if request.method == 'POST':
#         cust_id = request.POST['cust_id']

#         customer = Customer.objects.get(id=cust_id)

#         customer.first_name = request.POST['first_name']
#         customer.last_name = request.POST['last_name']
#         customer.user_name = request.POST['user_name']
#         customer.password = request.POST['password']
#         customer.email = request.POST['email']
#         customer.phone = request.POST['phone']

#         customer.save()
    
#     return showCustomersPageView(request)

