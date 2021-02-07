from django.urls import path

from . import views


app_name = 'static_page'

urlpatterns = [
    path('contact-us', views.contact_us_view, name='contact-us'),
    
]