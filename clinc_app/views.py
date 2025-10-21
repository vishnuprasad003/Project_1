from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from pyexpat.errors import messages

from clinc_app.form import Department_form, patient_form, Doctor_form, LoginRegistration
from clinc_app.models import Department, Patient, Doctor


# Create your views here.
def index(request):
    return render(request,'index.html')
@login_required(login_url="Login_view")
def index1(request):
    return render(request,'index1.html')


# def Department1(request):
#     form=Department_form()
#     if request.method=='POST':
#         form2=Department_form(request.POST)
#         if form2.is_valid():
#             form2.save()
#
#     return render(request,'Department.html',{"data":form})

# def patient1(request):
#     form = patient_form()
#     if request.method=='POST':
#         form2=patient_form(request.POST)
#         if form2.is_valid():
#             form2.save()
#
#     return  render(request,'patient.html',{"data":form})


# def Doctor1(request):
#     form = Doctor_form()
#     if request.method=='POST':
#         form2=Doctor_form(request.POST)
#         if form2.is_valid():
#             form2.save()
#
#     return render(request,"doctor.html",{"data":form})

# def department_view(request):
#     data=Department.objects.all()
#
#     return render(request,"views.html",{"view":data})

# def delete_data(request,id):
#     data=Department.objects.get(id=id)
#     data.delete()
#     return redirect("view1")

# def update_data(request,id):
#     data =Department.objects.get(id=id)
#
#
#
#     form1=Department_form(instance=data)
#
#     if request.method=="POST":
#         form2=Department_form(request.POST,instance=data)
#         if form2.is_valid():
#             form2.save()
#         return redirect("view1")
#     return render(request,"Department_udate.html",{"update":form1})

# def update_patient(request,id):
#     data=Patient.objects.get(id=id)
#     form=patient_form(instance=data)
#     if request.method=="POST":
#         form1=patient_form(request.POST,instance=data)
#         if form1.is_valid():
#             form1.save()
#         return  redirect("view1")
#     return render(request,"patient_update.html",{"update2":form})

# def delete_patient(request,id):
#     data=Patient.objects.get(id=id)
#     data.delete()
#     return redirect("view1")
#
# def patient_view(request):
#     data=Patient.objects.all()
#
#     return render(request,"patientdataview.html",{"view":data})
# def doctor_view(request):
#     data=Doctor.objects.all()
#     return render(request,"Doctordataview.html",{"view1":data})
# def update_doctor(request,id):
#     data=Doctor.objects.get(id=id)
#     form=Doctor_form(instance=data)
#     if request.method=="POST":
#         form1=Department_form(request.POST,instance=data)
#         if form1.is_valid():
#             form1.save()
#         return redirect("view1")
#     return render(request,"doctor_update.html",{"update3":form})
# def delete_doctor(request):
#     data=Doctor.objects.all()
#     data.delete()
#     return redirect("view1")

def doctor_add(request):
    form1=LoginRegistration()
    form2=Doctor_form()

    if request.method =='POST':
        form3=LoginRegistration(request.POST)
        form4 =Doctor_form(request.POST)

        if form3.is_valid() and form4.is_valid():

            data=form3.save(commit=False)
            data.is_doctor=True
            data.save()

            data1=form4.save(commit=False)
            data1.user=data
            data1.save()

            return redirect("Login_view")


    return render(request,"login2.html",{"form1":form1,"form2":form2})

def patient_add(request):
    form_data=LoginRegistration()
    form_data2=patient_form()

    if request.method =='POST':
        form3=LoginRegistration(request.POST)
        form4 =patient_form(request.POST)

        if form3.is_valid() and form4.is_valid():

            data=form3.save(commit=False)
            data.is_patient=True
            data.save()

            data1=form4.save(commit=False)
            data1.user=data
            data1.save()

            return redirect("Login_view")


    return render(request,"login3.html",{"form_data":form_data,"form_data2":form_data2})
@login_required(login_url="Login_view")
def admin_base(request):
    return render(request,"admin/adminBase.html")
@login_required(login_url="Login_view")
def doctor_base(request):
    return render(request,"doctor/doctorBase.html")
@login_required(login_url="Login_view")
def patient_base(request):
    return render(request,"patient/patientBase.html")


def login_view(request):
    if request.method=="POST":
        username=request.POST.get('uname')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect("base1")
            elif user.is_doctor:
                return redirect("base2")
            elif user.is_patient:
                return redirect("base3")
        # else:
             # messages.info(request,'invalid credentials ')
    return render(request,"login.html")

# def detail(request):
#     user_data = request.user
#
#     doc = Doctor.objects.get(user=user_data)
#     print(doc.id)
#     print(doc.Doctor_name)
#     print(doc.Doctor_department)


def logout_fun(request):
    logout(request)
    return redirect('new')
