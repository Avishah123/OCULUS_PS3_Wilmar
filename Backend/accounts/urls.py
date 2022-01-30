from django.contrib import admin
from django.urls import path
from . import views
from .views import *
from django.contrib import admin
from . import views
from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home,name='home'),
    path('enduser', views.organizer.as_view(), name='enduser'),
    path('stock', views.event_view, name='stock'),
    path('login', auth_views.LoginView.as_view(
        template_name='forms/login.html'), name='login'),
    path('test', views.form_rendering_test, name='test'),
    path('dashboard', views.dashboard, name='dashboard'),
    
     
   
] + static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT)