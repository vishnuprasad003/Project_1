from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from clinc_app.filters import departmentFilter
from clinc_app.form import Doctor_form, patient_form, Appointment_form
from clinc_app.models import Patient, Department, Doctor, doctor_shedule, BookingAppointment


@login_required(login_url="Login_view")
def profileViewP(request):
    user_data = request.user

    patient = Patient.objects.get(user=user_data)
    return render(request,"patient/ProfilePatient.html",{"data":patient})

@login_required(login_url="Login_view")
def editP(request,id):
    doct = Patient.objects.get(id=id)
    form1 = patient_form(instance=doct)
    if request.method=="POST":
        form=patient_form(request.POST,instance=doct)
        if form.is_valid():
            form.save()
        return redirect("profileViewP")
    return render(request, "patient/editprofile.html", {"data": form1})
@login_required(login_url="Login_view")
def department_booking(request):
    data= Department.objects.all()
    department_filter=departmentFilter(request.GET,queryset=data)
    data1=department_filter.qs
    context={

        'schedule':data1,
        'department_filter':department_filter

    }
    return render(request,"patient/bookingDetails.html",context)
@login_required(login_url="Login_view")
def FilterDoctor(request,id):
    data=Doctor.objects.filter(Doctor_Department=id)

    return render(request,"patient/filterDoctor.html",{"data1":data})
@login_required(login_url="Login_view")
def view_schedule(request,id):
    data=doctor_shedule.objects.filter(doctor=id)
    schedule_list=[]

    for schedule in data:

        bookingCount=BookingAppointment.objects.filter(doctor=id,scheduleTime=schedule)
        count=len(bookingCount)
        print(count)
        schedule_list.append(count)

        count_and_data = zip(data,schedule_list)

    return render(request,"patient/doctor_schedule_view.html",{"data_with_count":count_and_data})

@login_required(login_url="Login_view")
def Appointment(request,id):
    user_data = request.user
    patient_data = Patient.objects.get(user=user_data)
    schedule_data = doctor_shedule.objects.get(id=id)
    Doctor_details=schedule_data.doctor
    bookingCount=BookingAppointment.objects.filter(doctor = Doctor_details,scheduleTime = schedule_data)

    count = len(bookingCount)
    print(count)
    if count<10:
        obj=BookingAppointment()
        obj.doctor=Doctor_details
        obj.patient=patient_data
        obj.scheduleTime=schedule_data
        obj.save()
        return redirect("BookingDetailView")
    else:
        messages.info(request ,"No slot available")
        return redirect("FilterSchedule",id=Doctor_details.id)

    # return render(request,"patient/new_scheduleView.html",{"data1":schedule_data})
@login_required(login_url="Login_view")
def booking_details_view(request):
    user_data=request.user
    booking_detailsView=Patient.objects.get(user=user_data)
    data=BookingAppointment.objects.filter(patient=booking_detailsView)
    return render(request,"patient/bookingDetailsView.html",{"bookingDetailView":data})
@login_required(login_url="Login_view")
def delete_booking_details(request,id):
    data=BookingAppointment.objects.get(id=id)
    data.delete()
    return redirect("BookingDetailView")






