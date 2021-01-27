from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .forms import UserForm
from .models import Course
# Create your views here.

def index(request):
    job = Course.objects.latest("pk")
    a = request.user
    data = {"title":job.title, "start_date":job.start_date, "user":a}
    return render(request, "index.html",context=data)

class CoursesDetailView(DetailView):
    model = Course
    template_name = "courses.html"
    queryset = Course.objects.all()
    context_object_name = "course"


