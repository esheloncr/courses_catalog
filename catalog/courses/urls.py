from django.urls import path
from django.views.generic import TemplateView
from .views import CoursesDetailView, index
urlpatterns = [
    path("",index),
]