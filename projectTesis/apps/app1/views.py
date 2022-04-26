import email
from http.client import HTTPResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import response
#from matplotlib.style import context
from .filters import *
from .models import *
#from projectTesis.apps.app1.models import Patient
from .forms import *
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
import numpy as np
import joblib

# Create your views here.
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('Prediction')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Account was created for'+user)
                return redirect('login')
        context = {'form':form}
        return render(request,'register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('Prediction')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Prediction')
            else:
                messages.info(request, 'Username or Password is incorrect')
        context = {}
        return render(request,'login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def editUser(request):
    form = EditUserForm(instance = request.user)
    print(request.user)
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was updated for '+user)
            #return redirect('prediction')
    context = {'form':form}
    return render(request,'edit_user.html',context)

def changeUserPass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            #form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('Prediction')
        else:
            form = PasswordChangeForm(user=request.user)
        context = {'form':form}
        return render(request,'change_user_pass.html',context)

reloadModel = joblib.load('aiModels/LGModel.pkl')

"""
def prediction1(request):
    context = {'a' : 'Hola'}
    
    if request.method == 'POST':
        print('ola')
        print(type(float(request.POST.get('age'))))
        temp = np.array([
            float(request.POST.get('age')),
            float(request.POST.get('sex')),
            float(request.POST.get('chestPainType')),
            float(request.POST.get('restingBP')),
            float(request.POST.get('cholesterol')),
            float(request.POST.get('fastingBS')),
            float(request.POST.get('restingECG')),
            float(request.POST.get('maxHR')),
            float(request.POST.get('exerciseAngina')),
            float(request.POST.get('oldpeak')),
            float(request.POST.get('sT_Slope')),
        ])
        prediction = reloadModel.predict(temp.reshape(1, -1))[0]
        context = {'prediction':prediction}
    print('ola')
    
    return render(request,'prediction.html',context)
"""
def patientList(request):
    user = request.user
    patients = Patient.objects.filter(user=user)
    filter = PatientFilter(request.GET,queryset=patients)
    patients = filter.qs
    context = {'patient_list':patients,'filter':filter}
    return render(request,"patient_list.html",context)

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

def patientDetail(request, pk):
    patient = get_object_or_404(Patient,pk=pk,user=request.user)
    form = DetailPatientForm(instance=patient)
    context = {"patient":patient,"form":form}
    return render(request, 'patient_detail1.html',context)

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

def patientDelete(request, pk):
    patient = get_object_or_404(Patient,pk=pk,user=request.user)
    patient.delete()
    return redirect('patient_list')

def prediction(request):
    form = PredictionForm()
    prediction = 0
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            temp = np.array([
            form.cleaned_data['age'],
            form.cleaned_data['sex'],
            form.cleaned_data['chestPainType'],
            form.cleaned_data['restingBP'],
            form.cleaned_data['cholesterol'],
            form.cleaned_data['fastingBS'],
            form.cleaned_data['restingECG'],
            form.cleaned_data['maxHR'],
            form.cleaned_data['exerciseAngina'],
            form.cleaned_data['oldpeak'],
            form.cleaned_data['sT_Slope'],
            ])
            prediction = reloadModel.predict(temp.reshape(1, -1))[0]
            #form.save()
    context = {'form': form,'prediction':prediction}
    return render(request, 'prediction.html',context)
"""
def predictHD(request):
    print("holaaaaaaa")
    if request.method == 'POST':
        temp = np.array([
            request.POST.get('age'),
            request.POST.get('sex'),
            request.POST.get('chestPainType'),
            request.POST.get('restingBP'),
            request.POST.get('cholesterol'),
            request.POST.get('fastingBS'),
            request.POST.get('restingECG'),
            request.POST.get('maxHR'),
            request.POST.get('exerciseAngina'),
            request.POST.get('oldpeak'),
            request.POST.get('sT_Slope'),
        ])
        prediction = reloadModel.predict(temp.reshape(1, -1))[0]
    context = {'prediction':prediction}
    return render(request,'prediction.html',context)
"""