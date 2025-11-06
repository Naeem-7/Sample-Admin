from django.db import models
from django.contrib.auth.models import User

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=20)
    department = models.CharField(max_length=50)
    status = models.CharField(max_length=20, default='Pending')

class RecruiterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    email = models.EmailField()
    status = models.CharField(max_length=20, default='Pending')

class Application(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    recruiter = models.ForeignKey(RecruiterProfile, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100)
    status = models.CharField(max_length=50)

