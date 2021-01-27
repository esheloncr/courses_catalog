from django import forms
from .models import Course

class UserForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ("title","description","course_url","start_date","end_date",)
