from django.contrib import admin
from .models import StudentProfile

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'reg_no', 'department', 'status')
    search_fields = ('name', 'reg_no', 'department')
    list_filter = ('department', 'status')
