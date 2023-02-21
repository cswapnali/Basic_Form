from django import forms  
from .models import BasicForm
from django.core.exceptions import ValidationError
import re
from datetime import date

class Basic_Form(forms.ModelForm):
    class Meta:
        model = BasicForm
        fields = '__all__'
        labels = {
            'name': 'Name',
            'email': 'Email',
            'phone': 'Phone Number',
            'bday': 'Birthday'     
        }  
        widgets = {
            'bday': forms.widgets.DateInput(attrs={'type': 'date'}),
        }
    
    def clean_name(self):
        name = self.cleaned_data['name']
        if not name.isalpha():
            raise ValidationError("Name can only contain Alphabets!")
        return name
    
    def clean_email(self):
        email = self.cleaned_data["email"]
        patt = r'\b[A-Za-z0-9._%+-]+@[A-Za-z.-]+\.[A-Z|a-z]{2,3}\b'
        if (re.fullmatch(patt, email)):
            pass
        else:
            raise ValidationError("Invalid Email!")
        return email
    
    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        if phone:
            if not phone.isdigit():
                raise forms.ValidationError("Phone number can only contain digits.")
            if len(phone) != 10:
                raise forms.ValidationError("Phone number must be 10 digits.")
        return phone
    
    def clean_bday(self):
        bday = self.cleaned_data["bday"]
        today = date.today()
        age = today.year - bday.year - ((today.month, today.day) < (bday.month, bday.day))
        
        if age < 18:
            raise forms.ValidationError("You must be at least 18 years old to fill this form!")
        return bday
    
    