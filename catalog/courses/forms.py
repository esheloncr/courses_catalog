from django import forms
from .models import Course

class UserForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ("title","description","start_date","end_date",)

class SearchForm(forms.Form):
    query = forms.CharField()
