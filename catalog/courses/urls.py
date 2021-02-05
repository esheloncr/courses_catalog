from django.urls import path
from django.views.generic import TemplateView
from .views import CoursesDetailView, new_course, catalog, CourseEdit,CourseDelete, post_search,test

urlpatterns = [
    path("course/<int:pk>/",CoursesDetailView.as_view(), name="courses"),
    path("new",new_course),
    path("", catalog),
    #path("course/<int:pk>/edit",CourseEdit.as_view()),
    path("course/<int:pk>/edit",CourseEdit.as_view()),
    path("course/<int:pk>/delete",CourseDelete.as_view()),
    path("search",post_search),
    path("test", test),
    ]