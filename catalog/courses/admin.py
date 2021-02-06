from django.contrib import admin
from .models import Course
# Register your models here.


@admin.register(Course)
class AdminCourse(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date',)
    list_filter = ('course_id', 'start_date', 'end_date')
    fieldsets = (
        (None, {
            'fields': ('title','description', "author")
        }),
        ('Course date', {
            'fields': ('start_date', 'end_date')
        }),
    )

