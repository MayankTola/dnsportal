from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .inventory_form import *
from .models import *
from .remote_login import *


# Create your views here.


@login_required()
def inventory_form(request):
    form=site_form()
    # form = site_form(request.POST)
    if request.method == "POST":
        if form.is_valid():
            raw=form.cleaned_data
            data=site_details(location=raw['location'],management_ip=raw['management_ip'],site_address=raw['site_address'],spoc_name1=raw['spoc_name1'],spoc_contact1=raw['spoc_contact1'],spoc_name2=raw['spoc_name2'],spoc_contact2=raw['spoc_contact2'])
            data.save()
        else:
            print(form.errors)

    return render(request, "inventory_form.html", {"form": form})

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


def inventory_view(request):
    obj=vip_details.objects.filter()
    print(type(obj))
    # mp=obj.management_ip
    # vp=obj.virtual_ip
    # des=obj.description
    # print(list(obj))
    return render(request, "inventory_results.html", {"obj":obj})