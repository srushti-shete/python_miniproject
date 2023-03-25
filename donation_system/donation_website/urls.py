from django.contrib import admin
from django.urls import path 
from donation_website import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    path('', views.index , name = 'index'),
    path('About.html', views.About, name='About'),
    path('Contact.html', views.contact, name='Contact'),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

