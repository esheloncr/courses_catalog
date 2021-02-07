from django.urls import path
from .views import CoursesDetailView, catalog, CourseEdit, CourseDelete, post_search, NewCourse, test,login_user, NewUser

urlpatterns = [
    path("course/<int:pk>/",CoursesDetailView.as_view(), name="courses"),
    path("new",NewCourse.as_view()),
    path("", catalog),
    path("course/<int:pk>/edit",CourseEdit.as_view()),
    path("course/<int:pk>/delete",CourseDelete.as_view()),
    path("search",post_search),
    path("test", test),
    path("register",NewUser.as_view()),
    path("login",login_user)
    ]