from email import message
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.core.exceptions import ValidationError

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from email.mime.image import MIMEImage
from django.core.mail import EmailMultiAlternatives
import datetime


class EnduserSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)    
    mobile_number = forms.CharField(required=True)
    email = forms.CharField(required=True)
    
    field_order = ['username','first_name','mobile_number','email','password1','password2']

        
    class Meta(UserCreationForm.Meta):
        model = User
    

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_enduser = True
    
        user.save()
        enduser = Enduser.objects.create(user=user)
        enduser.first_name = self.cleaned_data.get('first_name')
        enduser.mobile_number = self.cleaned_data.get('mobile_number')
        enduser.email = self.cleaned_data.get('email')
        enduser.save()

        return user
    
    
def current_user(request):
    x = request.user
    return x


class stockform(forms.ModelForm):
    # stock_ticker = forms.ModelChoiceField(required=True,queryset=nse_bse_stocks.objects.all())
    # dividend_percetage = forms.CharField(required=True)
    # stock_record_date =forms.CharField(required=True)
    # stock_announcement_date= forms.CharField(required=True)
    
    class Meta:
        model = ticker
        fields = ["stock_ticker"]
        
        
    @transaction.atomic  
    def save(self,request):       
        print('inside save function of ')
        
        attendance = ticker(stock_ticker=self.cleaned_data.get('stock_ticker'),
                            user=current_user(request))
       
        attendance.save()
    