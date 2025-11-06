from django.shortcuts import render, redirect
from .models import StudentProfile, RecruiterProfile, Application

def admin_dashboard(request):
    students = StudentProfile.objects.all()
    recruiters = RecruiterProfile.objects.all()
    applications = Application.objects.all()

    context = {
        'students': students,
        'recruiters': recruiters,
        'total_students': students.count(),
        'total_recruiters': recruiters.count(),
        'total_applications': applications.count(),
    }
    return render(request, 'adminpanel/admin_dashboard.html', context)

def approve_student(request, student_id):
    student = StudentProfile.objects.get(id=student_id)
    student.status = 'Approved'
    student.save()
    return redirect('admin_dashboard')

def approve_recruiter(request, recruiter_id):
    recruiter = RecruiterProfile.objects.get(id=recruiter_id)
    recruiter.status = 'Approved'
    recruiter.save()
    return redirect('admin_dashboard')
