from django import forms
from .models import Course


class UserForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ("title","description","start_date","end_date",)
        widgets = {
            "title": forms.TextInput(attrs={"class":"form-control"}),
            "description": forms.Textarea(attrs={"class":"form-control"}),
            "start_date": forms.TextInput(attrs={"class":"form-control"}),
            "end_date": forms.TextInput(attrs={"class":"form-control"}),
        }


class SearchForm(forms.Form):
    query = forms.CharField()
