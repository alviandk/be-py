from django.urls import path

from . import views


app_name = 'portfolio'

urlpatterns = [
    path('', views.portfolio_list_view, name='portfolio_list'),
    path('<slug>/', views.project_detail_view, name='portfolio_detail'),
]