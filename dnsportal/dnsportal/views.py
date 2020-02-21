from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.shortcuts import render
from .remote_login import *
from .inventory_form import *

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UsersLoginForm
from .forms import UsersRegisterForm


# @login_required
def login_page(request):
    form = UsersLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("/home/")
    return render(request, "form.html", {
        "form": form,
        "title": "Login",
    })


def register_view(request):
    form = UsersRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        password = form.cleaned_data.get("password")
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect("/accounts/login")
    return render(request, "form.html", {
        "title": "Register",
        "form": form,
    })

def logout_view(request):
	logout(request)
	return HttpResponseRedirect("/")


@login_required()
def home(request):
    return render(request, 'home.html')

# Functions for dns_lookup functionality
@login_required()
def dns_lookup(request):
    return render(request, "dns_lookup.html")

# Functions for dns_lookup results
@login_required()
def lookup_results(request):
    location = request.POST.get('location')
    domain = request.POST.get('domain')
    qt = request.POST.get('query_type')
    # location = str(location)
    # domain = str(domain)
    # qt = str(qt)
    query = "sh /home/Abhilash/nand/nntest.sh " + domain + ' ' + location + ' ' + qt
    (stdoutstring, stderrstring) = execute_ssh_command(host, port, username, password, None, None, query)
    context = {'output': stdoutstring}
    return render(request, "lookup_results.html", context)

@login_required()
def inventory_form(request):
    form=submission_form()
    # print("test form")
    if request.method == "POST":
        form = submission_form(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            loc=form.cleaned_data["location"]
            print(loc)
        else:
            print(form.errors)
        # location = submission_form.location
    return render(request, "inventory_form.html",{"form": form})
