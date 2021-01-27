from django import forms
from .models import Course

class UserForm(forms.Form):
    name = forms.CharField()

