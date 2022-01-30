from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_enduser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
class Enduser(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=254)
    mobile_number = models.CharField(max_length=254)
    email = models.CharField(max_length=254)
    
    def __str__(self):
        
        return self.first_name
    
class ticker(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)    
    stock_ticker =models.CharField(max_length=254)
    dividend_percetage =models.CharField(max_length=254)
    stock_record_date = models.CharField(max_length=254)
    stock_announcement_date =models.CharField(max_length=254)
    

class nse_bse_stocks(models.Model):
    stock_ticker =models.CharField(max_length=254)
    
class nse_bse_dividend_alerts(models.Model):
    Stock_ticker =models.CharField(max_length=254)
    dividend_type =models.CharField(max_length=254)
    dividend_precentage = models.CharField(max_length=254)
    date_announcement =models.CharField(max_length=254)
    date_record = models.CharField(max_length=254)
    ex_dividend_date = models.CharField(max_length=254)