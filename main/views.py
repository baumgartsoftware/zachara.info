from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from main.forms import LoginForm


# Create your views here.

def main_view(request):
    template_name = "main/index.html"
    return render(request, template_name)


def login_view(request):
    login_form = LoginForm(request.POST or None)
    template = 'main/login.html'
    msg = None

    if request.method == "POST":

        if login_form.is_valid():
            username = login_form.cleaned_data.get("username")
            password = login_form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/dashboard")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, template, {"form": login_form, "msg": msg})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url="/login")
def dashboard_view(request):
    return render(request, "main/dashboard.html")
