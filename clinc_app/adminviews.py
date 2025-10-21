from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from clinc_app.filters import departmentFilter, PatientFilter
from clinc_app.form import patient_form, Doctor_form, Department_form
from clinc_app.models import Patient, Doctor, Department, doctor_shedule, BookingAppointment

@login_required(login_url="Login_view")
def patient_view1(request):
    data=Patient.objects.all()


    return render(request,"admin/patientView.html",{"view":data})
@login_required(login_url="Login_view")
def doctor_view1(request):
    data=Doctor.objects.all()
    return render(request,"admin/doctorView.html",{"view1":data})
@login_required(login_url="Login_view")
def update_patient(request,id):
    data=Patient.objects.get(id=id)
    form=patient_form(instance=data)
    if request.method=="POST":
        form1=patient_form(request.POST,instance=data)
        if form1.is_valid():
            form1.save()
        return  redirect("view4")
    return render(request,"admin/patientUpdate.html",{"update2":form})
@login_required(login_url="Login_view")
def delete_patient(request,id):
    data=Patient.objects.get(id=id)
    data.delete()
    return redirect("view4")
@login_required(login_url="Login_view")
def update_doctor(request,id):
    data=Doctor.objects.get(id=id)
    form=Doctor_form(instance=data)
    if request.method=="POST":
        form1=Doctor_form(request.POST,instance=data)
        if form1.is_valid():
            form1.save()
        return redirect("view5")
    return render(request,"admin/doctorUpdate.html",{"update3":form})
@login_required(login_url="Login_view")
def delete_doctor(request):
    data=Doctor.objects.all()
    data.delete()
    return redirect("view5")

@login_required(login_url="Login_view")
def Department1(request):
    form=Department_form()
    if request.method=='POST':
        form2=Department_form(request.POST,request.FILES)
        if form2.is_valid():
            form2.save()

    return render(request,'admin/departmentadd.html',{"data":form})

@login_required(login_url="Login_view")
def department_view(request):
    data=Department.objects.all()
    department_filter = departmentFilter(request.GET,queryset=data)
    data1=department_filter.qs
    context={
        'schedule':data1,
        'department_filter':department_filter
    }

    return render(request,"admin/departmentView.html",context)

@login_required(login_url="Login_view")
def delete_data(request,id):
    data=Department.objects.get(id=id)
    data.delete()
    return redirect("view1")

@login_required(login_url="Login_view")
def update_data(request,id):
    data =Department.objects.get(id=id)
    form1=Department_form(instance=data)
    if request.method=="POST":
        form2=Department_form(request.POST,request.FILES,instance=data)
        if form2.is_valid():
            form2.save()
        return redirect("view1")
    return render(request,"admin/departmentUpdate.html",{"update":form1})

@login_required(login_url="Login_view")
def DoctorScheduleView(request):
    data=doctor_shedule.objects.all()
    return render(request,"admin/schedule_view.html",{"scheduleView":data})

@login_required(login_url="Login_view")
def scheduleDelete(request,id):
    data=doctor_shedule.objects.get(id=id)
    data.delete()
    return redirect("base1")

@login_required(login_url="Login_view")
def booking_details_view(request):
    data=BookingAppointment.objects.all()
    return render(request,"admin/BookingDetailsView.html",{"booking_details_view":data})
