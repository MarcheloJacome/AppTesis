from http.client import HTTPResponse
from django.shortcuts import render
from django.http import response
from .forms import *
import numpy as np
import joblib

reloadModel = joblib.load('aiModels/LGModel.pkl')
# Create your views here.

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

def predictHD(request):
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
