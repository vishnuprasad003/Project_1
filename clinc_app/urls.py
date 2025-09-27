from django.urls import path

from clinc_app import views, adminviews, doctorviews, patientviews

urlpatterns = [
    path('',views.index,name="new"),
    path('index1',views.index1,name="index1"),
    path('Login_view',views.login_view,name="Login_view"),

    path('Department',adminviews.Department1,name="Department_name"),
    path('departmentview',adminviews.department_view,name="view1"),
    path('delete/<int:id>/',adminviews.delete_data,name="delete"),
    path('update/<int:id>/',adminviews.update_data,name="update"),

    path('formLogin',views.doctor_add,name="viewLogin"),
    path('patientLogin',views.patient_add,name="patientLogin"),

    path('patientUpdate/<int:id>/',adminviews.update_patient,name="PatientUpdate"),
    path('deletePatient/<int:id>/',adminviews.delete_patient,name="deletePatient"),

    path('doctorUpdate/<int:id>/',adminviews.update_doctor,name="DoctorUpdate"),
    path('deleteDoctor/<int:id>/',adminviews.delete_doctor,name="deleteDoctor"),

    path('adminBasePage',views.admin_base,name="base1"),
    path('doctorBasePage',views.doctor_base,name="base2"),
    path('patientBasePage',views.patient_base,name="base3"),

    path('adminViewP',adminviews.patient_view1,name="view4"),
    path('adminViewDo',adminviews.doctor_view1,name="view5"),

    path('detail',doctorviews.detail,name="detail"),
    path('detailP',doctorviews.Patient_Details,name="detailP"),
    path('editD/<int:id>/',doctorviews.edit,name="editD"),

    path('profileViewP', patientviews.profileViewP, name="profileViewP"),
    path('editP/<int:id>/', patientviews.editP, name="editP"),
    path('department_booking',patientviews.department_booking,name="department_booking")

]