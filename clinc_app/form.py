from django import forms
from django.contrib.auth.forms import UserCreationForm

from clinc_app.models import Patient, Department, Doctor, Login


class LoginRegistration(UserCreationForm):
    username=forms.CharField()
    password1=forms.CharField(label="password",widget=forms.PasswordInput)
    password2 = forms.CharField(label="conformPassword", widget=forms.PasswordInput)

    class Meta:
        model =Login
        fields =('username','password1','password2')


class patient_form(forms.ModelForm):

    class Meta:
        model =Patient
        fields ="__all__"
        exclude =('user',)

class Department_form(forms.ModelForm):

    class Meta:
        model =Department
        fields ="__all__"

class Doctor_form(forms.ModelForm):

    class Meta:
        model = Doctor
        fields ="__all__"
        exclude = ('user',)
