from django.urls import path

from . import views


app_name = 'course'

urlpatterns = [
    path('', views.course_list_view, name='course_list'),
    path('course-group-list/', views.course_group_list_view, name='course_group_list'),
    path('course-group-detail/', views.course_group_detail_view, name='course_group_detail'), 
    path('course-mentor-list/', views.course_mentor_list_view, name='course_mentor_list'),
    path('course-mentor-detail/<int:id>/', views.course_mentor_detail_view, name='course_mentor_detail'),
    path('course-mentoring-private/', views.course_mentoring_private_view, name='course_mentoring_private'), 
    path('course-college-final-project/', views.course_college_final_project_view, name='course_college_final_project'), 
    path('<course_slug>/module/<slug>/', views.module_detail_view, name='module_detail'),    
    path('<slug>/', views.course_detail_view, name='course_detail'),
]