from django.urls import path
from django.views.generic import TemplateView
from .views import CoursesDetailView, index

urlpatterns = [
    path("courses/<int:pk>/",CoursesDetailView.as_view(), name="courses"),
    path("",index)
]