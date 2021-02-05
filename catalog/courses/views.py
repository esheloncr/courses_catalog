from django.shortcuts import render
from django.views.generic import DetailView,ListView,UpdateView,DeleteView,CreateView
from django.http import HttpResponseRedirect
from django.contrib.postgres.search import SearchVector
from .forms import UserForm, SearchForm
from .models import Course
# Create your views here.

class NewCourse(CreateView):
    model = Course
    form_class = UserForm
    template_name = "new.html"
    def form_valid(self, form):
        if form.is_valid():
            form.save()
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

def test(request):
    return render(request, "new_edit.html")

"""class CoursesListView(ListView):
    model = Course
    queryset = Course.objects.all()
    template_name = "main.html"
    context_object_name = "courses"""


