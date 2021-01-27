from django.urls import path
from django.views.generic import TemplateView
from .views import CoursesDetailView, index, new_course, CoursesListView

urlpatterns = [
    path("courses/<int:pk>/",CoursesDetailView.as_view(), name="courses"),
    path("",index),
    path("new",new_course),
    path("main",CoursesListView.as_view()),
]