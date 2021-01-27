from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .forms import UserForm
from .models import Course
# Create your views here.

def index(request):
    job = Course.objects.earliest("pk")
    print(request.user)
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            job.description = userform.cleaned_data["name"]
    else:
        pass
    data = {"title":job.title,"descr":job.description, "start_date":job.start_date, "end_date":job.end_date,"forms":userform}
    return render(request, "index.html",context=data)

class CoursesDetailView(DetailView):
    model = Course
    template_name = "index.html"
    queryset = Course.objects.all()


