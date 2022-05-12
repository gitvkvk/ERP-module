from django import forms
from django.forms import ModelForm
from .models import PurchaseOrder
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime



class PurchaseOrderAddForm(forms.Form):

    

    """put below, the fields of the form that are sent to the view, which then are saved to the view fields, then saved to model"""
    ProjectEntry = forms.CharField(help_text = "proeeeeject here")
    SupplierEntry = forms.CharField(help_text = "supplier here")
    NotesEntry = forms.CharField(help_text = "notes here")


    def clean_ProjectEntry (self):
            projectdata = self.cleaned_data('ProjectEntry')
            return projectdata

    def clean_SupplierEntry (self):
            supplierdata = self.cleaned_data('SupplierEntry')
            return supplierdata
    
    def clean_NotesEntry (self):
            notesdata = self.cleaned_data('NotesEntry')
            return notesdata
            

    class Meta: 
        model = PurchaseOrder
        fields = ['project','supplier' ,'notes']
        



"""
class PurchaseOrder(forms.Form):

    project = forms.CharField(initial = 'enter project number', )
    supplier = forms.CharField(initial = 'enter supplier name', )
    typePO = forms.ChoiceField(max_length=1, choices=TYPEPO, default='M')
    notes = forms.CharField(initial = 'enter notes here', )

    def clean_project(self):
        data = self.cleaned_data['project']

        if data == "ketchup":

            raise ValidationError(_('Invalid condiment, please do not type ketchup'))
            
        return data

"""


