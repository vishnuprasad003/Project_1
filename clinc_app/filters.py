import django_filters
from django import forms



from clinc_app.models import Department, Patient


class departmentFilter(django_filters.FilterSet):
    Department_name=django_filters.CharFilter(label="",lookup_expr='icontains',widget=forms.TextInput(attrs={'placeholder':'search Department','class':'form-control'}))


    class Meta:
        model=Department
        fields=('Department_name',)

class PatientFilter(django_filters.FilterSet):
    Patient_phone_no = django_filters.CharFilter(label="",lookup_expr='icontains',widget=forms.TextInput(attrs={'placeholder':'search Patient','class':'form-control'}))

    class Meta:
        model=Patient
        fields=('Patient_phone_no','Patient_blood_group',)

