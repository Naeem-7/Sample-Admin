from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('approve/student/<int:student_id>/', views.approve_student, name='approve_student'),
    path('approve/recruiter/<int:recruiter_id>/', views.approve_recruiter, name='approve_recruiter'),
]
