from django.urls import path
from django.views.generic import TemplateView
from .views import CoursesDetailView, index, new_course, CoursesListView, CourseEdit,CourseDelete

urlpatterns = [
    path("courses/<int:pk>/",CoursesDetailView.as_view(), name="courses"),
    path("",index),
    path("new",new_course),
    path("main",CoursesListView.as_view()),
    path("courses/<int:pk>/edit",CourseEdit.as_view()),
    path("courses/<int:pk>/delete",CourseDelete.as_view()),
]