from django.shortcuts import render
from time import timezone
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.views.generic import CreateView
from django.contrib.auth import login
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
import csv
from django.http import HttpResponse
from django.contrib import auth
from .models import *
from django.template.loader import render_to_string
import datetime

from django.forms import ValidationError
from django.contrib import messages
# Create your views here.
from django.contrib.auth.decorators import login_required
import pandas as pd 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import schedule
import time
from bs4 import BeautifulSoup
import time
from datetime import datetime
import csv
import pandas as pd
from selenium.webdriver.support.ui import Select




# we have to use the USER table to access the id of the user and not the Enduser


def home(request):
    x = Enduser.objects.all()
    y = User.objects.all()
    for i in y:
        print(i.id)
            
    print(request.user)
    return render(request,'home.html')


def form_rendering_test(request):
    languages  = nse_bse_stocks.objects.all()
    return render(request,'forms/test.html',{"languages":languages})

@login_required
def dashboard(request):
    stock_ticker = ticker.objects.filter(user=request.user)
    context = {
        'stock_ticker' : stock_ticker,
        
    }
    return render(request,'dashboard.html',context)

def scraper():
    url = 'https://www.moneycontrol.com/stocks/marketinfo/dividends_declared/index.php'

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')



    chrome_browser = webdriver.Chrome('accounts/chromedriver.exe',options=options)

    chrome_browser.get(url)
    ddelement= Select(chrome_browser.find_element_by_xpath('//*[@id="sel_year"]'))
    ddelement.select_by_value('2021')

    go_button = chrome_browser.find_element_by_xpath('//*[@id="bonus_frm"]/div/table/tbody/tr/td[3]/input')
    go_button.click()

    time.sleep(10)

    html = chrome_browser.page_source

    df = pd.read_html(html)

    print(df)



class organizer(CreateView):
    model = User
    form_class = EnduserSignUpForm
    template_name = 'forms/test.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)       

        return redirect('home')


@login_required
def event_view(request):
    languages  = nse_bse_stocks.objects.all()    
    context ={
        "languages":languages,
    }
     
    # create object of form
    form = stockform(request.POST or None, request.FILES or None)
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        
        form.save(request)
        return redirect('home')
  
    context['form']= form
    return render(request, "forms/stock_form.html", context)
