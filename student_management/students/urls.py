from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('students/',views.student_list,name='student_list'),
    path('student/add/', views.student_create, name='student_create'),
    path('students/',views.student_list, name='student_list'),
    path('student/add/',views.student_form,name='student_form'),
    path('students/update/<int:id>/', views.student_update, name='student_update'),
    path('students/delete/<int:id>/', views.student_delete, name='student_delete'),
    path('api-page/',views.api_student_page,name='api_student_page'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),


]
