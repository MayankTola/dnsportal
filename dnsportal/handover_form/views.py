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
        form = HandOver_form(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    return render(request, "handover_form/handover_form.html", {"form": form})


@login_required()
def handover_view(request):
    content = handover_details.objects.all()
    return render(request, "handover_form/handover_view.html", {'content': content})


@login_required()
def handover_edit(request, id):
    content = handover_details.objects.get(id=id)
    return render(request, 'handover_form/handover_edit.html', {'content': content})


@login_required()
def handover_update(request, id):
    content = handover_details.objects.get(id=id)
    form = HandOver_form(request.POST, instance=content)
    if form.is_valid():
        form.save()
        return redirect("/handover_form/view")
    return render(request, 'handover_form/handover_edit.html', {'content': content})
