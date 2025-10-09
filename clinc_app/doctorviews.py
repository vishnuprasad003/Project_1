from django.shortcuts import render, redirect

from clinc_app.filters import PatientFilter
from clinc_app.form import Doctor_form, doctor_shedule_form
from clinc_app.models import Doctor, Patient, doctor_shedule


def detail(request):
    user_data = request.user

    doc = Doctor.objects.get(user=user_data)
    return render(request,"doctor/profile.html",{"data":doc})



def edit(request,id):

    doct = Doctor.objects.get(id=id)
    form1 = Doctor_form(instance=doct)
    if request.method=="POST":
        form=Doctor_form(request.POST,instance=doct)
        if form.is_valid():
            form.save()
        return redirect("detail")
    return render(request, "doctor/profileEdit.html", {"data": form1})

def Patient_Details(request):
    data = Patient.objects.all()
    patient_details=PatientFilter(request.GET,queryset=data)
    data1=patient_details.qs
    context={
        'schedule':data1,
        'patient_details':patient_details,
    }


    return render(request, "doctor/searchPatient.html", context)

def doctor_schedules(request):
    user_data= request.user
    sche= Doctor.objects.get(user=user_data)
    form=doctor_shedule_form()
    if request.method=="POST":
        data1=doctor_shedule_form(request.POST)
        if data1.is_valid():
            schedule=data1.save(commit=False)
            schedule.doctor=sche
            schedule.save()
            return redirect("base2")

    return render(request,"doctor/doctor_schedule.html",{"data":form})
def scheduleViewD(request):
    user_data= request.user
    scheduleView=Doctor.objects.get(user=user_data)
    data=doctor_shedule.objects.filter(doctor=scheduleView)

    return render(request,"doctor/schedule_view.html",{"scheduleview":data})
def scheduleDelete(request,id):
    data=doctor_shedule.objects.get(id=id)
    data.delete()
    return redirect("scheduleViewD")



