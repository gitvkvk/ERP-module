from django.shortcuts import get_object_or_404, render
from valsamis.models import PurchaseOrder
from valsamis.models import ship, company
from django.http import HttpResponse, HttpResponseRedirect
from . import forms
from .forms import  PurchaseOrderAddForm
from django.views import generic

class POListView(generic.ListView):
    model = PurchaseOrder

class PODetailView(generic.DetailView):
    model = PurchaseOrder

def PurchaseOrderAddView(request):

    """def PurchaseOrderAddView(request,pk):"""
    """should be named purchase order add view"""


    form = PurchaseOrderAddForm()
    
    """Purchase_Order = get_object_or_404(PurchaseOrder, pk=pk)"""
    """does PO model need a pk?"""
    
    if request.method == 'POST':
       
        form = PurchaseOrderAddForm(request.POST)

        if form.is_valid():
            form.save()

            """
            Purchase_Order.project = form.cleaned_data['ProjectEntry']
            Purchase_Order.supplier = form.cleaned_data['SupplierEntry']
            Purchase_Order.notes = form.cleaned_data['NotesEntry']

            write data fields to be saved from PO model here
           """
            return HttpResponseRedirect(reverse('PurchaseOrderAdd'))
        else:
            return HttpResponse()
    
    else:
            form = PurchaseOrder()

    context = {
        'form':form,
        'Purchase_Order': PurchaseOrder,
        }

    return render(request, 'PurchaseOrderAdd.html', context)

    """context=context?"""


"""from valsamis.forms import PurchaseOrder


addPO form

def PurchaseOrder(request):
   
    # If this is a POST request then process the Form data
    if request.method == 'POST':

        form = PurchaseOrder(request.POST)

        if form.is_valid():
            PurchaseOrder.project = form.cleaned_data['project']
            PurchaseOrder.supplier = form.cleaned_data['supplier']
            PurchaseOrder.typePO = form.cleaned_data['typePO']
            PurchaseOrder.notes = form.cleaned_data['notes']

             linking the Model.Field  to the Form.Field above


            book_instance.save()
            return HttpResponseRedirect('addPO' ) 

    else:
        projectvariable = 3
        form = PurchaseOrder(request) issue with what goes here

    context = {
        'form': form,
        'PurchaseOrder': PurchaseOrder,
    }

    return render(request, 'urls/addPO.html', context)

"""



"""valsamis Base pages"""

def index(request):
    return render(request, 'index.html')

def databases(request):
    return render(request, 'databases.html')

def formspage(request):
    return render(request, 'forms.html')




"""list views, later django-filters"""

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

def companyformview(request):
    form = forms.companyform()
    if request.method == 'POST':
        form = forms.companyform(request.Post)
        html = 'we have recieved this form again'
    else:
        html = 'welcome for the first time'
    return render(request, 'companyform.html', {'html': html, 'form' : form })


"""form views for adding"""


