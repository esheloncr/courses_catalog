from django.shortcuts import render,redirect
from django.views.generic import DetailView,UpdateView,DeleteView,CreateView
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.postgres.search import SearchVector
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserForm, SearchForm, RegisterUser
from .models import Course
# Create your views here.


class NewUser(CreateView):
    model = User
    form_class = RegisterUser
    template_name = "register.html"

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        else:
            return self.form_valid()
        return HttpResponseRedirect("/")


def login_user(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Username or password are incorrect")
    return render(request, "login.html",context)

class NewCourse(CreateView):
    model = Course
    form_class = UserForm
    template_name = "new.html"

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(self.request,"Account has been created" + user)
        else:
            return self.form_valid()
        return HttpResponseRedirect("/")


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


def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Course.objects.annotate(
                search=SearchVector('title', 'body'),
            ).filter(search=query)
    return render(request,
                  'main.html',
                  {'form': form,
                   'query': query,
                   'results': results})


def catalog(request):
    return render(request, "index.html")


class CoursesDetailView(DetailView):
    model = Course
    template_name = "course.html"
    queryset = Course.objects.all()
    context_object_name = "course"


class CourseEdit(UpdateView):
    model = Course
    template_name = "new_edit.html"
    form_class = UserForm

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        else:
            return self.form_valid()
        return HttpResponseRedirect("/")


class CourseDelete(DeleteView):
    model = Course
    success_url = '../../'
    template_name = "new_edit.html"


# Test func
def test(request):
    return render(request, "test.html")
