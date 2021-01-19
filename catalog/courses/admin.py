from django.contrib import admin
from .models import Course
# Register your models here.


class AdminCourse(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date','course_url')
    list_filter = ('course_id', 'start_date', 'end_date')
    fieldsets = (
        (None, {
            'fields': ('title','description','course_url')
        }),
        ('Course date', {
            'fields': ('start_date', 'end_date')
        }),
    )


admin.site.register(Course,AdminCourse)