from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import *
from .models import *


# Create your views here.

@login_required()
def handover_form(request):
    form = HandOver_form()  # form called from forms.py
    if request.method == "POST":
        form = HandOver_form(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("/handover_form")
        else:
            print(form.errors)
    return render(request, "handover_form/handover_form.html", {"form": form})


@login_required()
def handover_view(request, func):
    if func == "ravpn":
        a = "RAVPN"
    elif func == "dns":
        a = "DNS"
    else:
        a = "Network Devices"
    content = handover_details.objects.filter(function=a)
    return render(request, "handover_form/handover_view.html", {'content': content, 'title': a})


@login_required()
def handover_edit(request, id):
    content = handover_details.objects.get(id=id)
    form = HandOver_form(request.POST or None, instance=content)
    return render(request, 'handover_form/handover_update.html', {'form': form, 'content': content})


@login_required()
def handover_update(request, id):
    content = handover_details.objects.get(id=id)
    form = HandOver_form(request.POST or None, instance=content)
    if form.is_valid():
        a = form.cleaned_data['function']
        if a == "RAVPN":
            b = 'ravpn'
        elif a == "DNS":
            b = 'dns'
        else:
            b = 'network'
        form.save()
        return redirect("/handover_form/view/" + b)
    return render(request, 'handover_form/handover_update.html', {'form': form, 'content': content})
