from django.urls import path

from . import views


app_name = 'static_page'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('contact-us', views.contact_us_view, name='contact-us'),   
    path('learn-type', views.learn_type_view, name='learn_type'),
    path('about-us', views.about_view, name='about-us'),
    
]