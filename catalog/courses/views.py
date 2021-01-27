from django.shortcuts import render, redirect
from django.views.generic import DetailView,ListView
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserForm
from .models import Course
# Create your views here.

def index(request):
    course = Course.objects.latest("pk")
    user = request.user
    data = {"title":course.title, "start_date":course.start_date, "user":user}
    return render(request, "index.html",context=data)

def new_course(request):
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            userform.save()
            title = userform.cleaned_data['title']
            description = userform.cleaned_data['description']
            start_date = userform.cleaned_data['start_date']
            end_date = userform.cleaned_data['end_date']
            author = request.user
            return HttpResponseRedirect('/')
    else:
        userform = UserForm()
    return render(request, "new.html",{"form":userform})

def edit_course(request):
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            a = Course.objects.get(pk=1)
            f = Course(request.POST, instance=a)
            f.save()
            return HttpResponseRedirect('/')
    else:
        userform = UserForm()
    return render(request, "courses.html",{"form":userform})

class CoursesDetailView(DetailView):
    model = Course
    template_name = "courses.html"
    queryset = Course.objects.all()
    context_object_name = "course"
    #extra_context = {"delete":queryset.delete()}

class CoursesListView(ListView):
    model = Course
    queryset = Course.objects.all()
    template_name = "main.html"
    context_object_name = "courses"

