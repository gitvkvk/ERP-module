from django.shortcuts import get_object_or_404, redirect, render
from valsamis.models import PurchaseOrder
from valsamis.models import ship, company
from django.http import HttpResponse, HttpResponseRedirect
from . import forms
from .forms import shipform
from django.views import generic


#CRUD operations for ship

def shiplist(request):
    context = {'ship_list' : ship.objects.all()}
    return render(request, "valsamis/shiplist.html", context)

def shipformview(request, id = 0):
    if request.method == "GET":
        if id==0:                                            #if true, it is insert operation
                form = shipform()
        else:                                                #update operation
                shipvar = ship.objects.get(pk=id)
                form = shipform(instance=shipvar)       
        return render(request, "valsamis/shipformpage.html", {"form":form})

    else: # POST requests
        if id == 0:
            form = shipform(request.POST)
        else:
            shipvar = ship.objects.get(pk=id)
            form = shipform(request.POST, instance = shipvar)
        if form.is_valid():
            form.save()
        return redirect('/valsamis/shiplist')

def shipdelete(request, id):
    shipvar = ship.objects.get(pk=id)
    shipvar.delete()
    return redirect('/valsamis/shiplist') 


#generic list and detail view

class POListView(generic.ListView):
    model = PurchaseOrder

class PODetailView(generic.DetailView):
    model = PurchaseOrder


#valsamis base page views

def index(request):
    return render(request, 'index.html')

def databases(request):
    return render(request, 'databases.html')

def formspage(request):
    return render(request, 'forms.html')



#list views, later use django-filter

def branchview(request): 
    num_ship = ship.objects.all().count()
    context = {
            'num_ship' : num_ship,
            }
    return render(request, 'branchview.html', context=context)

def projectview(request):
    return render(request, 'projectview.html')

def customerview(request):
    return render(request, 'customerview.html')
