from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Course
# Create your views here.


def index(request):
    course_title = Course.objects.latest("title")
    course_descr = Course.objects.order_by('-course_id')
    data = {"title":"Каталог курсов","course_title":course_title, "description":course_descr}
    return render(request, 'index.html', context=data)


class CoursesDetailView(DetailView):
    model = Course
    template_name = "index.html"
    queryset = Course.objects.all()


