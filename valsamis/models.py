from queue import Empty
from django.db import models
from django.urls import reverse
import uuid
import django.utils.timezone
from django.contrib.auth.models import User


#PAGINATION https://realpython.com/django-pagination/


class generalitem(models.Model):
    name = models.CharField(max_length=200, help_text='Enter the general item name') #unique = True
    date_created = models.DateTimeField(auto_now = True) #vs auto_now_add ? #https://stackoverflow.com/questions/51389042/difference-between-auto-now-and-auto-now-add
    def __str__(self):
        return self.name

class ship(models.Model):
    created_user = models.ForeignKey(
                        User,
                        default = 1,
                        null = True, 
                        on_delete = models.SET_NULL
                        ) # https://www.geeksforgeeks.org/associate-user-to-its-upload-post-in-django/
    #add a date edited field                
    edited_user = models.ForeignKey(
                        User, 
                        related_name='edited_user', 
                        default = 1, 
                        null = True, 
                        on_delete = models.SET_NULL)
    #add a time edited field

    name = models.CharField(max_length=200)
    company = models.ForeignKey('company', on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now = True)
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
    name = models.CharField(max_length=200, help_text='Enter the company name')
    date_created = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.name
    
class customer(models.Model):
    name = models.CharField(max_length=200, help_text='Enter the customer name')
    date_created = models.DateTimeField(auto_now = True)
    """Need contact name"""
    """Need contact number""" 
    def __str__(self):
        return self.name
    
class supplier(models.Model):
    name = models.CharField(max_length=200, help_text='Enter the supplier name')
    date_created = models.DateTimeField(auto_now = True)
    """Need user created"""
    """Need contact name="""
    """Need contact number""" 
    """Need address""" 
    """Need zip""" 
    """Need fax number""" 
    """Need PO box number""" 
    """Need country""" 
    def __str__(self):
        return self.name

    
class project(models.Model):
    id = models.BigAutoField(primary_key=True)
    #copyfield = models.IntegerField(id)
    name = models.TextField(max_length=200, help_text='Enter the project name')
    date_created = models.DateTimeField(auto_now = True)
    ship = models.ForeignKey('ship', on_delete=models.CASCADE, null=True) #PREVIOUSLY was models.RESTRICT
    # could use on_delete = models.SET_NULL
    company = models.ForeignKey('company', on_delete=models.SET_NULL, null=True)
    notes = models.TextField(max_length=1000, help_text='any notes for the project', blank=True, null=True)
    """need to have searchable project code"""
    customer = models.ForeignKey('customer', on_delete=models.SET_NULL, null=True)
    """need start date"""
    """need end date"""
    """need date created"""
    """need user created"""
    """need budget"""
    def __str__(self):
        return self.name


class PurchaseOrder(models.Model):
    TYPEPO = (
        ('M', 'Material'),
        ('L', 'Logistics'),
        ('T', 'Travel'),
        ('O', 'Other'),
    )
    pochoices = models.CharField(max_length=1, choices=TYPEPO, blank=True, default='M', help_text="Type of PO")
    project = models.ForeignKey('project', on_delete=models.CASCADE) #PREVIOUSLY was models.RESTRICT
    customer = models.ForeignKey('customer', default= '',  on_delete=models.CASCADE)#added default ='' to fix issue back filling entries 
    #can also delete migrations, flush sqlight command, create new superuser
    supplier = models.ForeignKey('supplier', on_delete=models.CASCADE) #PREVIOUSLY was models.RESTRICT
    date_created = models.DateTimeField(auto_now = True)
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
    """id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for purchase')"""
    PurchaseOrder = models.ForeignKey('PurchaseOrder', on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now = True)
    item_description = models.TextField(max_length=1000, help_text='Enter the description of the item', null=True)
    generalitem = models.ForeignKey('generalitem', on_delete=models.CASCADE, null=True)
    unit= models.CharField(max_length=20)
    price= models.DecimalField(max_digits=19, decimal_places=10)
    currency = models.CharField(max_length=1, choices=TYPECURRENCY, default ='U')
    supplier_code= models.CharField(max_length=40, blank=True, help_text='Enter Supplier Code if you can')
    notes = models.TextField(max_length=1000,help_text ='Enter any notes for this item')
    #make notes optional
    def __str__(self):
        return f'{self.id} ({self.item_description})'


