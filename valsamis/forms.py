from django import forms
from django.forms import ModelForm
from .models import ship
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime


class shipform(forms.ModelForm):

        class Meta:
                model = ship
                fields ='__all__'
                labels = {
                  'typeship' : 'What type of ship?',     
                }
        def __init__(self, *args, **kwargs):
             super(shipform, self).__init__(*args, **kwargs)
             self.fields['company'].empty_label = "SelectDropDown"  


