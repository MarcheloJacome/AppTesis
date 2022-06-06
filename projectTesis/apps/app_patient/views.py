from django.shortcuts import render, redirect, get_object_or_404
from .filters import PatientFilter
from .models import Patient
from .forms import CreatePatientForm, DetailPatientForm
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login")
def patientList(request):
    user = request.user
    patients = Patient.objects.filter(user=user)
    filter = PatientFilter(request.GET,queryset=patients)
    patients = filter.qs
    context = {'patient_list':patients,'filter':filter}
    return render(request,"patient_list.html",context)

@login_required(login_url="/login")
def patientCreate(request):
    form = CreatePatientForm()
    if request.method == 'POST':
        form = CreatePatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.user = request.user
            patient.save()
            return redirect('patient_list')
    context = {'form':form}
    return render(request,'patient_create.html',context)

@login_required(login_url="/login")
def patientDetail(request, pk):
    patient = get_object_or_404(Patient,pk=pk,user=request.user)
    form = DetailPatientForm(instance=patient)
    context = {"patient":patient,"form":form}
    return render(request, 'patient_detail.html',context)

@login_required(login_url="/login")
def patientEdit(request, pk):
    patient = get_object_or_404(Patient,pk=pk,user=request.user)
    form = CreatePatientForm(instance=patient)
    if request.method == 'POST':
        form = CreatePatientForm(request.POST,instance=patient)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.user = request.user
            patient.save()
            return redirect('patient_list')
    context = {"patient":patient,"form":form}
    return render(request, 'patient_edit.html',context)

@login_required(login_url="/login")
def patientDelete(request, pk):
    patient = get_object_or_404(Patient,pk=pk,user=request.user)
    patient.delete()
    return redirect('patient_list')

