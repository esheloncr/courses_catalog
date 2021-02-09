from django.urls import path
from .views import CoursesDetailView, catalog,edit_course,delete_course, new_course, test,login_user,logoutUser, register

urlpatterns = [
    path("course/<int:pk>/",CoursesDetailView.as_view(), name="courses"),
    path("new",new_course),
    path("", catalog,name="index"),
    path("course/<str:pk>/edit",edit_course, name="edit"),
    path("course/<int:pk>/delete",delete_course, name="delete"),
    path("test", test),
    path("register",register, name="register"),
    path("login",login_user, name="login"),
    path("logout",logoutUser, name="logout")
    ]