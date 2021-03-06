from django.urls import path

from . import views


app_name = 'testimonial'

urlpatterns = [
    path('', views.testimonial_list_view, name='testimonial_list'),
    path('<int:testimonial_id>/', views.testimonial_detail_view, name='testimonial_detail'),    
]