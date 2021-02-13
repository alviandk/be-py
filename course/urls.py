from django.urls import path

from . import views


app_name = 'course'

urlpatterns = [
    path('', views.course_list_view, name='course_list'),
    path('<slug>/', views.course_detail_view, name='course_detail'),    
]