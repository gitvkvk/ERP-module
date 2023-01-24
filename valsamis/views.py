from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from valsamis.models import ship, company, MaterialItemRegister, PurchaseOrder
from django.http import HttpResponse, HttpResponseRedirect
from . import forms
from .forms import shipform, POform
from django.views import generic
from django.contrib.auth.models import User
from .filters import UserFilter
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# antiquated examples
# class POListView(generic.ListView):
#     model = PurchaseOrder    
# class PODetailView(generic.DetailView):
#     model = PurchaseOrder


#BASE PAGES
#valsamis base pages
def index(request):
    return render(request, 'index.html')
def databases(request):
    return render(request, 'databases.html')
def reportspage(request):
    return render(request, 'reports.html')
#delete this later, only as examples
def branchview(request): 
    num_ship = ship.objects.all().count()
    context = {
            'num_ship' : num_ship,
            }
    return render(request, 'branchview.html', context=context)
def customerview(request):
    return render(request, 'customerview.html')


#SHIP
#ship list
#ship form (handles updates also)
#ship delete
def shiplist(request):
    context = {'ship_list' : ship.objects.all()}
    return render(request, "valsamis/shiplist.html", context)
def shipformview(request, id = 0):
    if request.method == "GET":
        if id==0:                                            #blank form
                form = shipform()
        else:                                                #populated form
                shipvar = ship.objects.get(pk=id)
                form = shipform(instance=shipvar)       
        return render(request, "valsamis/shipformpage.html", {"form":form})

    else: # POST requests
        if id == 0:
            form = shipform(request.POST)                   #create ship

        else:                                                  #update ship
            shipvar = ship.objects.get(pk=id)
            form = shipform(request.POST, instance = shipvar) #combine instance with form post params
        if form.is_valid():
            #form.save() original, added the below to add who created/modified item last
            obj = form.save(commit = False)
            if id == 0:
                obj.created_user = request.user
                #timestamp
                obj.save()
            else:
                obj.edited_user = request.user
                #timestamp
                obj.save()
        return redirect('/valsamis/shiplist')
def shipdelete(request, id):
    shipvar = ship.objects.get(pk=id)
    shipvar.delete()
    return redirect('/valsamis/shiplist') 


#PO filter view
#Material filter view (and detail of PO view)
#PO form (handles updates also)
#PO delete
#PO PDF print
def POFilterListView(request):
    qs = PurchaseOrder.objects.all()
    #can inport another model besides purchase order also
    #getting the named parameters from the HTML from the GET request, saving into variables
    contains_project_query = request.GET.get('project_contains')
    id_exact_query = request.GET.get('id_exact')
    supplier_customer_query = request.GET.get('supplier_or_customer')

    if contains_project_query != '' and contains_project_query is not None: #if it is not empty string and not None
        qs = qs.filter(project__name__icontains = contains_project_query) #models case sensitive? for forein key, drill down with __
        #can filter material item register, supplier_id, id, project_id
        #icontains is case insensitive, contains is not

    elif id_exact_query != '' and id_exact_query is not None: 
        qs = qs.filter(id = id_exact_query) 
    
    elif supplier_customer_query != '' and supplier_customer_query is not None: 
        qs = qs.filter( Q(supplier__name__icontains = supplier_customer_query) | Q(customer__name__icontains = supplier_customer_query)
         ).distinct() 
         #query can return results from both of or statements, returning same post twice. need distinct

    context = {
        'queryset': qs
        #can have another model passed into context dictionary
    }

    return render(request, "pofilterview.html", context)
def MaterialItemRegisterView(request, pk = 0):
    if pk == 0:
        qs = MaterialItemRegister.objects.all()
        context = {
        'queryset': qs
        }
        return render(request, "POitemdetails", context)

    else:
        #get query, add to context, render table
        qs = MaterialItemRegister.objects.all()
        qs = qs.filter(PurchaseOrder = pk)
        context = {
        'queryset': qs
        }
        return render(request, "POitemdetails", context)
def POformview(request, id = 0):
    if request.method == "GET":
        if id==0:                                            #if true, it is insert operation
                form = POform()  #MAKE PO FORM
        else:                                                #update operation
                POvar = PurchaseOrder.objects.get(pk=id)
                form = POform(instance=POvar)       
        return render(request, "valsamis/POformpage.html", {"form":form})  # POformpage.html

    else: # POST requests
        if id == 0:
            form = POform(request.POST)
        else:
            POvar = PurchaseOrder.objects.get(pk=id)
            form = POform(request.POST, instance = POvar)
        if form.is_valid():
            form.save()
        return redirect('/valsamis/POfilterlistview') #HAD TO change this to match the pre-named LIST VIEW
def POdelete(request, id):
    POvar = PurchaseOrder.objects.get(pk=id)
    POvar.delete()
    return redirect('/valsamis/POfilterlistview') # POdelete.html
def POpdfview (request):

    #create bytestream buffer
    buf = io.BytesIO()
    #create a canvas
    c =canvas.Canvas(buf, pagesize=letter, bottomup=0)
    #create text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)


    dataforPDF = MaterialItemRegister.objects.all() #make this a query instead

    #dataforPDF2 = PO register....

    #create blank list
    lines = []

    for x in dataforPDF:
        #lines.append(x.PurchaseOrder)
        lines.append(x.item_description)
        # lines.append(x.generalitem)
        lines.append(x.unit)
        #lines.append(x.price)
        #lines.append(x.currency)
       # lines.append(x.supplier_code)
        #lines.append(x.notes)
       # lines.append(" ")

    for line in lines:
        textob.textLine(line)

    #finish up
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf,as_attachment=True, filename = 'POPDF.pdf' )



#django-filter tutorial
def search(request):
    user_list = User.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'valsamis/user_list.html', {'filter': user_filter})


def BootstrapFilterView(request):

    qs = PurchaseOrder.objects.all()
    #can inport another model besides purchase order also

    #getting the named parameters from the HTML from the GET request, saving into variables
    contains_project_query = request.GET.get('project_contains')
    id_exact_query = request.GET.get('id_exact')
    supplier_customer_query = request.GET.get('supplier_or_customer')
    print(contains_project_query)

    if contains_project_query != '' and contains_project_query is not None: #if it is not empty string and not None
        qs = qs.filter(project__name__icontains = contains_project_query) #models case sensitive? for forein key, drill down with __
        #can filter material item register, supplier_id, id, project_id
        #icontains is case insensitive, contains is not

    elif id_exact_query != '' and id_exact_query is not None: 
        qs = qs.filter(id = id_exact_query) 
    
    elif supplier_customer_query != '' and supplier_customer_query is not None: 
        qs = qs.filter( Q(supplier__name__icontains = supplier_customer_query) | Q(customer__name__icontains = supplier_customer_query)
         ).distinct() 
         #query can return results from both of or statements, returning same post twice. need distinct

    context = {
        'queryset': qs
        #can have another model passed into context dictionary
    }
    return render(request, "bootstrap_form.html", context)

#new views

#takes to....
#need URL reverse for this