from django import forms
from django.forms import ModelForm
from .models import PurchaseOrder, ship
from django.core.exceptions import ValidationError
import datetime


class shipform(forms.ModelForm):
        class Meta:
                model = ship
                #fields ='__all__'
                fields = [
                        'name',
                        'company',
                        'reviewed',
                        'typeship'

                ]
                labels = {
                  'typeship' : 'What type of ship?',     
                }

        def __init__(self, *args, **kwargs):
             super(shipform, self).__init__(*args, **kwargs)
             self.fields['company'].empty_label = "SelectDropDown"  


class POform(forms.ModelForm):

        class Meta:
                model = PurchaseOrder
                fields ='__all__'
               
        def __init__(self, *args, **kwargs):
             super(POform, self).__init__(*args, **kwargs)
             self.fields['project'].empty_label = "SelectDropDown"  


