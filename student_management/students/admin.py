from django.contrib import admin
from .models import Student, Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = ('id', 'course_name', 'duration', 'fees')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'email',
        'phone',
        'age',
        'course',
        'joined_date'
    )

    search_fields = ('name', 'email')

    list_filter = ('course',)