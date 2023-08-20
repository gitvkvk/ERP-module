from queue import Empty
from django.db import models
from django.urls import reverse
import uuid
import django.utils.timezone
from django.contrib.auth.models import User

from django.db.models import Sum

from django.utils import timezone
import qrcode #https://www.youtube.com/watch?v=xk8K3MNu81I&t=621s #for making QR code
from io import BytesIO #for making QR code
from django.core.files import File #for making QR code
from PIL import Image, ImageDraw #for making QR code


#PAGINATION https://realpython.com/django-pagination/


class generalitem(models.Model):
    name = models.CharField(max_length=200) #unique = True
    category = models.CharField(max_length=200, default = "testing") #unique = True
    group = models.CharField(max_length=200, default = "testing") #unique = True
    subgroup = models.CharField(max_length=200, default = "testing") #unique = True
    date_created = models.DateTimeField(auto_now = True)  #https://stackoverflow.com/questions/51389042/difference-between-auto-now-and-auto-now-add
    #version
    #visability
    #locked
    def __str__(self):
        return self.name

"""
is this like a detail view of each database item?
                    what about super interlinked records?

if not using detail fk:
    how to link new record (w/new version) to old record?

    version = on create, 0
        on edit, increment version
            when delete, set visability to 0 (for previous records also)
            on modify, create new record

        display only latest version
        when doing analytics on record, only on most recent version
        
"""



class ship(models.Model):
    date_created = models.DateTimeField(auto_now_add = True)
    created_user = models.ForeignKey(
                        User,
                        default = 1,
                        null = True, 
                        on_delete = models.SET_NULL
                        ) # https://www.geeksforgeeks.org/associate-user-to-its-upload-post-in-django/
    date_edited = models.DateTimeField(auto_now = True)               
    edited_user = models.ForeignKey(
                        User, 
                        related_name='edited_user', 
                        default = 1, 
                        null = True, 
                        on_delete = models.SET_NULL)
    #having list of edits, when edit is made
    #check the instance as unactive, having a stack of hidden edits per instance for reverting data
    #also would want to track what actual change was made
    #instead of updating the form: move old form to unactive, copy data w/ new into new entry, active
    #locking entries so no editing from outside, or even from inside for certain items
    name = models.CharField(max_length=200)
    company = models.ForeignKey('company', on_delete=models.SET_NULL, null=True)
    views = models.IntegerField(default = 0)
    reviewed = models.BooleanField(default = 0)
    SHIP_LIST = (
        ('Cruise ship', 'cruise ship'), #stored value vs displayed in drop down value
        ('Tanker', 'tanker'),
        ('Passenger Ship', 'passenger Ship'),
        ('Other', 'other'),
    )
    typeship = models.CharField(
        max_length=100, #previously 1, with c -> cruise ship, t -> tanker, ETC
        choices=SHIP_LIST,
        blank=True,
        default='Cruise ship',
    )


    def is_user_this(edited_user):
        if edited_user == "cats":
            pass
        else:
            pass

    def __str__(self):
        return self.name


class company(models.Model):
    date_created = models.DateTimeField(auto_now_add = True)
    """created_user = models.ForeignKey(
                        User,
                        default = 1,
                        null = True, 
                        on_delete = models.SET_NULL
                        ) # https://www.geeksforgeeks.org/associate-user-to-its-upload-post-in-django/
    date_edited = models.DateTimeField(auto_now = True)               
    edited_user = models.ForeignKey(
                        User, 
                        #related_name='edited_user', 
                        default = 1, 
                        null = True, 
                        on_delete = models.SET_NULL)"""
    name = models.CharField(max_length=200, help_text='Enter the company name')
    type  = models.CharField(max_length=200, help_text='Enter the type of company (ship, ...)', default = "testing")
    contact_info  = models.CharField(max_length=200, help_text='Enter the contact info (optional)', default = "testing")
    location_info  = models.CharField(max_length=200, help_text='Enter the location (optional)', default = "testing")
    def __str__(self):
        return self.name
    
class customer(models.Model):
    date_created = models.DateTimeField(auto_now_add = True)
    """created_user = models.ForeignKey(
                        User,
                        default = 1,
                        null = True, 
                        on_delete = models.SET_NULL
                        ) # https://www.geeksforgeeks.org/associate-user-to-its-upload-post-in-django/
    date_edited = models.DateTimeField(auto_now = True)               
    edited_user = models.ForeignKey(
                        User, 
                        #related_name='edited_user', 
                        default = 1, 
                        null = True, 
                        on_delete = models.SET_NULL)"""
    name = models.CharField(max_length=200, help_text='Enter the customer name')
    address1 = models.CharField(max_length=200, help_text='Enter the customer address', default = "testing")
    phone = models.CharField(max_length=200, help_text='Enter the customer phone number', default = "testing")
    email = models.CharField(max_length=200, help_text='Enter the customer email', default = "testing")
    country = models.CharField(max_length=200, help_text='Enter the customer country', default = "testing")
    PObox = models.CharField(max_length=200, help_text='Enter the customer PO box', default = "testing")
    notes = models.CharField(max_length=200, help_text='Enter any notes about this customer', default = "testing")
    def __str__(self):
        return self.name
    
#could make supplier contact model that links to the supplier, for a list of contacts w/ names, emails, numbers, etc
class supplier(models.Model):
    date_created = models.DateTimeField(auto_now_add = True)
    """created_user = models.ForeignKey(
                        User,
                        default = 1,
                        null = True, 
                        on_delete = models.SET_NULL
                        ) # https://www.geeksforgeeks.org/associate-user-to-its-upload-post-in-django/
    date_edited = models.DateTimeField(auto_now = True)               
    edited_user = models.ForeignKey(
                        User, 
                        #related_name='edited_user', 
                        default = 1, 
                        null = True, 
                        on_delete = models.SET_NULL)"""
    name = models.CharField(max_length=200, help_text='Enter the supplier name')
    address1 = models.CharField(max_length=200, help_text='Enter the supplier address', default = "testing")
    phone = models.CharField(max_length=200, help_text='Enter the supplier phone number', default = "testing")
    email = models.CharField(max_length=200, help_text='Enter the supplier email', default = "testing")
    country = models.CharField(max_length=200, help_text='Enter the supplier country', default = "testing")
    PObox = models.CharField(max_length=200, help_text='Enter the supplier PO box', default = "testing")
    notes = models.CharField(max_length=200, help_text='Enter any notes about this supplier', default = "testing")
    """Need contact name="""
    """Need contact number""" 
    def __str__(self):
        return self.name

    
class project(models.Model):
    date_created = models.DateTimeField(auto_now_add = True)
    """created_user = models.ForeignKey(
                        User,
                        default = 1,
                        null = True, 
                        on_delete = models.SET_NULL
                        ) # https://www.geeksforgeeks.org/associate-user-to-its-upload-post-in-django/
    date_edited = models.DateTimeField(auto_now = True)               
    edited_user = models.ForeignKey(
                        User, 
                        #related_name='edited_user', 
                        default = 1, 
                        null = True, 
                        on_delete = models.SET_NULL)"""
    id = models.BigAutoField(primary_key=True)
    #need to have code system like current 23-200-...
    #copyfield = models.IntegerField(id)
    name = models.TextField(max_length=200, help_text='Enter the project name')
    manager = models.TextField(max_length=200, help_text='Enter the project manager', default = "testing") #change this to User model user
    ship = models.ForeignKey('ship', on_delete=models.CASCADE, null=True) #PREVIOUSLY was models.RESTRICT
    # could use on_delete = models.SET_NULL
    company = models.ForeignKey('company', on_delete=models.SET_NULL, null=True)
    notes = models.TextField(max_length=1000, help_text='any notes for the project', blank=True, null=True)
    embarkation = models.TextField(max_length=100, help_text='embarkation port', blank=True)
    disembarkation = models.TextField(max_length=100, help_text='disembarkation port', blank=True)
    customer = models.ForeignKey('customer', on_delete=models.SET_NULL, null=True)
    project_start_date  = models.DateTimeField(blank = True, default = timezone.now) 
    project_end_date  = models.DateTimeField(blank = True, default = timezone.now)
    #define function: flags empty entries and shows in an alerts dashboard of missing information
    #start, end date, ....
    """need date created, user created, date edited, user edited, list of edits"""
    """need budget foreign key"""
    #need an upload portal
    TYPE_LIST = (
        ('Inspection', 'Inspection'), #stored value vs displayed in drop down value
        ('Dry Dock', 'Dry Dock'),
        ('Shop', 'Shop'),
        ('Fabrication', 'Fabrication'),
    )
    typeship = models.CharField(
        max_length=100, 
        choices=TYPE_LIST,
        blank=True,
        default='Inspection',
    )
    #reports for linking projects, assigning projects to projects
    #	https://stackoverflow.com/questions/55098356/how-can-i-relate-a-model-instance-to-another-in-django
    def __str__(self):
        return self.name

#BUDGET class model
"""
Budget/ BOQ items in budget
•	Item group
•	Item cost code
•	General item
•	Orders
•	MRF
•	Requisition
•	Project #
•	User created
•	Type of budget
o	Materials
o	Consumable
o	Labor
o	General expense
o	Shop expense
•	Description/notes
•	Name
•	Unit qty
•	Price/unit
•	Total$
•	Upload portal

"""

class PurchaseOrder(models.Model):
    TYPEPO = (
        ('M', 'Material'),
        ('L', 'Logistics'),
        ('T', 'Travel'),
        ('O', 'Other'),
    )
    date_created = models.DateTimeField(auto_now_add = True)
    """created_user = models.ForeignKey(
                        User,
                        default = 1,
                        null = True, 
                        on_delete = models.SET_NULL
                        ) # https://www.geeksforgeeks.org/associate-user-to-its-upload-post-in-django/
    date_edited = models.DateTimeField(auto_now = True)               
    edited_user = models.ForeignKey(
                        User, 
                        #related_name='edited_user', 
                        default = 1, 
                        null = True, 
                        on_delete = models.SET_NULL)"""
    pochoices = models.CharField(max_length=1, choices=TYPEPO, blank=True, default='M')
    project = models.ForeignKey('project', on_delete=models.CASCADE) #PREVIOUSLY was models.RESTRICT
    customer = models.ForeignKey('customer', default= '',  on_delete=models.CASCADE)#added default ='' to fix issue back filling entries 
    #can also delete migrations, flush sqlight command, create new superuser
    supplier = models.ForeignKey('supplier', on_delete=models.CASCADE) #PREVIOUSLY was models.RESTRICT
    """POtype = models.CharField(max_length=1, choices=TYPEPO, default='M')"""
    notes = models.TextField(max_length=1000, help_text='any notes for PO?', blank=True, null=True)
    #many to many field with general item? a general item can have many PO and PO can have many general item? No
    #each material item has one PO, can have a gen item tag (tag links to mat item links to PO) PO__materialitemregister__generalitem__name
    #this is drill down structure, but what if you want to see what POs a general item has been assigned to?
    #do you drill down every PO searching for item 
    #or
    #do you use many to many to see what POs item has?
    def __str__(self):
        return f'{self.id} ({self.project})'

    def get_absolute_url(self):
        return reverse('purchase-order-detail', args=[str(self.id)]) #passing id arguement to URL with name p-o-d, into the view
    def getPOcost(self):
        pass
        #takes id, adds together item register

class MaterialItemRegister(models.Model):
    TYPECURRENCY = (
        ('U', 'US Dollars'),
        ('E', 'Euros'),
        ('P', 'Pesos'),
    )
    date_created = models.DateTimeField(auto_now_add = True)
    """created_user = models.ForeignKey(
                        User,
                        default = 1,
                        null = True, 
                        on_delete = models.SET_NULL
                        ) # https://www.geeksforgeeks.org/associate-user-to-its-upload-post-in-django/
    date_edited = models.DateTimeField(auto_now = True)               
    edited_user = models.ForeignKey(
                        User, 
                        #related_name='edited_user', 
                        default = 1, 
                        null = True, 
                        on_delete = models.SET_NULL)"""
    """id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for purchase')"""
    PurchaseOrder = models.ForeignKey('PurchaseOrder', on_delete=models.CASCADE, null=True)
    item_description = models.TextField(max_length=1000, help_text='Enter the description of the item', null=True)
    generalitem = models.ForeignKey('generalitem', on_delete=models.CASCADE, null=True)
    unit= models.CharField(max_length=20)
    price= models.DecimalField(max_digits=19, decimal_places=2)
    currency = models.CharField(max_length=1, choices=TYPECURRENCY, default ='U')
    supplier_code= models.CharField(max_length=40, blank=True, help_text='Enter Supplier Code if you can')
    notes = models.TextField(max_length=1000,help_text ='Enter any notes for this item')
    qr_code = models.ImageField(upload_to='qr_codes', blank=True) 
    #could make notes a foreign key/detail view for the specific item, having a hyperlink in the PO table view to see note
    #make notes optional
    def __str__(self):
        return f'{self.id} ({self.item_description})'
    def get_absolute_url(self):
        return reverse('POitemfilterformURL', args=[str(self.PurchaseOrder.id)]) 
    def save(self, *args, **kwargs):
        qrcode_image = qrcode.make(self.id) #qr based on name field
        canvas = Image.new('RGB',  (290, 290), 'white') #construct new image based on parameters: mode, size, color
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_image) #paste QR image to canvas
        fname = f'qr_code_{self.id}.png'  #set a file name
        buffer = BytesIO() #create in memory file object
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save = False) #create a file object and pass it to image field
        #save = False otherwise infinite loop, many images in media files
        canvas.close()
        super().save(*args,**kwargs)

    
    
    #could include a PO total price function (split apart by currencies)
    #convert all items to chosen currency and have final price
    #call this function in view and save to queryset, with the input of the PO number desired from URL

    #put this in the PO model, so the (self) argument automatically gives PO id
    
  #  def get_PO_price(self):
   #     kevin = qs.aggregate(Sum('price'))
   #     return reverse('purchase-order-detail', args=[str(self.id)]) #passing id arguement to URL with name p-o-d, into the view
        




