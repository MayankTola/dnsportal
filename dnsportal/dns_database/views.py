from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import *
from .models import *
from .remote_login import *


# Create your views here.

# Functions for CRUD operations.

@login_required()
def inventory_form(request):
    form = site_form()
    if request.method == "POST":
        form = site_form(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    return render(request, "inventory_form.html", {"form": form})


@login_required()
def inventory_view(request):
    content = site_details.objects.all()
    return render(request, "inventory_results.html", {'content': content})


@login_required()
def inventory_edit(request, id):
    content = site_details.objects.get(id=id)
    form = site_form(request.POST or None, instance=content)
    return render(request, 'inventory_edit.html', {'content': content, 'form': form})


@login_required()
def inventory_update(request, id):
    content = site_details.objects.get(id=id)
    form = site_form(request.POST or None, instance=content)
    if form.is_valid():
        form.save()
        return redirect("/inventory/view")
    return render(request, 'inventory_edit.html', {'content': content})


@login_required()
def inventory_delete(request, id):
    content = site_details.objects.get(id=id)
    content.delete()
    return redirect("/inventory/view")

# host = '10.227.219.36'
# port = 22
# username = 'B0097262'
# password = 'Airtel@123'
# keyfile_path = 'private_key_file'
# # print(form.cleaned_data)
# query = "tmsh list ltm virtual all-properties | grep -i 'description\|destination' | sed -r 's/(:domain|.domain|destination |description |    )//g'"
# (stdoutstring, stderrstring) = execute_ssh_command(host, port, username, password, None, None, query)
# print(stdoutstring)
# for i in range(0,int(len(stdoutstring)),2):
#     data = vip_details(management_ip=host,virtual_ip=stdoutstring[i+1],description=stdoutstring[i])
#     data.save()
