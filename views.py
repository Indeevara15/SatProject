from django.http import HttpResponse
from django.shortcuts import render, redirect

from SatApp.models import SatData


# Create your views here.
def insert_fun(request):
    return render(request,'insert.html')


def insertdata_fun(request):
    s1 = SatData()
    s1.name = request.POST['txtname']
    s1.address = request.POST['txtaddress']
    s1.city = request.POST['txtcity']
    s1.country = request.POST['txtcountry']
    s1.pincode = request.POST['txtnumber']
    s1.sat_score = request.POST['txtscore']
    s1.save()



    return render(request,'insert.html',{'msg':'Successfully Added'})




def viewdata_fun(request):
    data = SatData.objects.all()
    return render(request,'viewdata.html',{'sat':data})


def update_fun(request,id):
    s1 = SatData.objects.get(id=id)
    if request.method == 'POST':
        s1.name = request.POST['txtname']
        s1.address = request.POST['txtaddress']
        s1.city = request.POST['txtcity']
        s1.country = request.POST['txtcountry']
        s1.pincode = request.POST['txtnumber']
        s1.sat_score = request.POST['txtscore']
        s1.save()
        return redirect('viewdata')
    else:
        return render(request, 'update.html', {'data': s1})


def del_fun(request,id):
    s1 = SatData.objects.get(id=id)
    s1.delete()
    return redirect('viewdata')
