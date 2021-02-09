from django.shortcuts import render,redirect
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserForm, RegisterUser
from .models import Course
# Create your views here.


def register(request):
    if request.user.is_authenticated:
        return redirect("index")
    if request.method == "POST":
        reg_form = RegisterUser(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            messages.success(request,"Успешная регистрация")
            return redirect("/")
    else:
        reg_form = RegisterUser()
    return render(request,"register.html", {"form":reg_form})


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
            messages.info(request,"Неверно введены логин или пароль")
    return render(request, "login.html",context)


@login_required(login_url="login")
def logoutUser(request):
    logout(request)
    return redirect("/")


@login_required(login_url="login")
def new_course(request):
    if request.method == "POST":
        create_form = UserForm(request.POST)
        if create_form.is_valid():
            create_form.save()
            title = create_form.cleaned_data['title']
            description = create_form.cleaned_data['description']
            start_date = create_form.cleaned_data['start_date']
            end_date = create_form.cleaned_data['end_date']
            messages.success(request,"Курс добавлен")
            return redirect("/")
    else:
        create_form = UserForm()
    return render(request,"new.html",{"form":create_form})


def catalog(request):
    return render(request, "index.html")


class CoursesDetailView(DetailView):
    model = Course
    template_name = "course.html"
    queryset = Course.objects.all()
    context_object_name = "course"


@login_required(login_url="login")
def edit_course(request,pk):
    course = Course.objects.get(course_id=pk)
    form = UserForm(instance=course)
    if request.method == "POST":
        form = UserForm(request.POST, instance=course)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(request,"new_edit.html",{"form":form})


@login_required(login_url="login")
def delete_course(request, pk):
    if not request.user.is_superuser and not request.user.is_staff:
        messages.error(request, "У вас нет прав для удаления")
        redirect("index")
        return redirect("index")
    course = Course.objects.get(course_id=pk)
    if request.method == "POST":
        course.delete()
        messages.success(request,"Успешно удалено")
        return redirect("index")
    return render(request, "course_delete.html",{"course":course})


# Test func
@login_required(login_url="login")
def test(request):
    return render(request, "test.html")
