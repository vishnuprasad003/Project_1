from django.shortcuts import render, redirect

from clinc_app.filters import departmentFilter
from clinc_app.form import Doctor_form, patient_form
from clinc_app.models import Patient, Department


def profileViewP(request):
    user_data = request.user

    patient = Patient.objects.get(user=user_data)
    return render(request,"patient/ProfilePatient.html",{"data":patient})


def editP(request,id):
    doct = Patient.objects.get(id=id)
    form1 = patient_form(instance=doct)
    if request.method=="POST":
        form=patient_form(request.POST,instance=doct)
        if form.is_valid():
            form.save()
        return redirect("profileViewP")
    return render(request, "patient/editprofile.html", {"data": form1})

def department_booking(request):
    data= Department.objects.all()
    department_filter=departmentFilter(request.GET,queryset=data)
    data1=department_filter.qs
    context={

        'schedule':data1,
        'department_filter':department_filter

    }
    return render(request,"patient/bookingDetails.html",context)