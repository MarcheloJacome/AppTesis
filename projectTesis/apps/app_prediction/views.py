from django.shortcuts import render, redirect, get_object_or_404
from .filters import PredictionFilter
from .models import Prediction, Patient
from .forms import PredictionForm, EditPredictionForm, MakePredictionForm, DetailPredictionForm
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required
import numpy as np
import pandas as pd
import joblib
import datetime


non_proc_labels = ['Age', 'Sex', 'ChestPainType', 'RestingBP', 'Cholesterol', 'FastingBS',
       'RestingECG', 'MaxHR', 'ExerciseAngina', 'Oldpeak', 'ST_Slope']

@login_required(login_url="/login")
def predictionList(request, pk):
    patient = get_object_or_404(Patient,pk=pk,user=request.user)
    #user = request.user
    predictions = Prediction.objects.filter(Patient=patient).order_by('-pk')
    filter = PredictionFilter(request.GET,queryset=predictions)
    predictions = filter.qs
    context = {'pred_list':predictions,'filter':filter,'patient':patient}
    return render(request,"prediction_list.html",context)

@login_required(login_url="/login")
def predictionCreate(request,pk):
    form = MakePredictionForm()
    patient = get_object_or_404(Patient,pk=pk,user=request.user)
    if request.method == 'POST':
        form = MakePredictionForm(request.POST)
        if form.is_valid():        
            #Getting data from post and shaping it to make prediction
            temp = np.array([[
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
            ]])
            temp_pd = pd.DataFrame(temp,columns=non_proc_labels)
            ohEncoder = joblib.load('aiModels/OHEncoder.pkl')
            transformed_temp = ohEncoder.transform(temp_pd)
            sScaler = joblib.load('aiModels/SScaler.pkl')
            sc_transformed_temp = sScaler.transform(transformed_temp)
            aimod = form.cleaned_data['aiModel']
            if aimod == 0 :
                #xgb_class = joblib.load('aiModels/XGBClassifier.pkl')
                mlp_classifier = joblib.load('aiModels/MLPClassifier.pkl')
                hdisease = mlp_classifier.predict(sc_transformed_temp)[0]
                hdProb = mlp_classifier.predict_proba(sc_transformed_temp)[0][1]*100
            else:
                svClassifier = joblib.load('aiModels/SVClassifier.pkl')
                hdisease = svClassifier.predict(sc_transformed_temp)[0]
                hdProb = svClassifier.predict_proba(sc_transformed_temp)[0][1]*100               
            patient = get_object_or_404(Patient,pk=pk)
            prediction = form.save(commit=False)
            prediction.date_created = datetime.date.today()
            prediction.Patient = patient
            prediction.heartDisease = int(hdisease)
            prediction.heartDiseaseProb = hdProb
            patient.last_prediction = int(hdisease)
            patient.last_prediction_prob = hdProb
            patient.save()
            prediction.save()
            return redirect('../prediction_detail'+'/'+str(prediction.pk))
    context = {'form':form,'patient':patient}
    return render(request,'prediction_create.html',context)

@login_required(login_url="/login")
def predictionDetail(request, pk):
    prediction = get_object_or_404(Prediction,pk=pk,Patient__user=request.user)
    form = DetailPredictionForm(instance=prediction)
    context = {"prediction":prediction,"form":form,"patient":prediction.Patient}
    return render(request, 'prediction_detail.html',context)

@login_required(login_url="/login")
def predictionEdit(request, pk):
    prediction = get_object_or_404(Prediction,pk=pk,Patient__user=request.user)
    form = EditPredictionForm(instance=prediction)
    #patient = get_object_or_404(Patient,pk=pk)
    if request.method == 'POST':
        form = EditPredictionForm(request.POST,instance=prediction)
        if form.is_valid():        
            #Getting data from post and shaping it to make prediction
            temp = np.array([[
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
            ]])
            temp_pd = pd.DataFrame(temp,columns=non_proc_labels)
            ohEncoder = joblib.load('aiModels/OHEncoder.pkl')
            transformed_temp = ohEncoder.transform(temp_pd)
            sScaler = joblib.load('aiModels/SScaler.pkl')
            sc_transformed_temp = sScaler.transform(transformed_temp)
            aimod = form.cleaned_data['aiModel']
            if aimod == 0 :
                #xgb_class = joblib.load('aiModels/XGBClassifier.pkl')
                mlp_classifier = joblib.load('aiModels/MLPClassifier.pkl')
                hdisease = mlp_classifier.predict(sc_transformed_temp)[0]
                hdProb = mlp_classifier.predict_proba(sc_transformed_temp)[0][1]*100
            else:
                svClassifier = joblib.load('aiModels/SVClassifier.pkl')
                hdisease = svClassifier.predict(sc_transformed_temp)[0]
                hdProb = svClassifier.predict_proba(sc_transformed_temp)[0][1]*100
            save_as_new = form.cleaned_data['newPrediction']
            prediction = form.save(commit=False)
            pk_patient = prediction.Patient.pk
            if save_as_new:
                patient = get_object_or_404(Patient,pk=pk_patient)
                prediction.pk = None
                prediction._state.adding = True
                prediction.date_created = datetime.date.today()
                prediction.heartDisease = int(hdisease)
                prediction.heartDiseaseProb = hdProb
                prediction.Patient = patient
                patient.last_prediction = int(hdisease)
                patient.last_prediction_prob = hdProb
                patient.save()
            else :
                prediction.heartDisease = int(hdisease)
                prediction.heartDiseaseProb = hdProb
            prediction.save()
            return redirect('../prediction_detail'+'/'+str(prediction.pk))
    context = {"prediction":prediction,"form":form,"patient":prediction.Patient}
    return render(request, 'prediction_edit.html',context)

@login_required(login_url="/login")
def predictionDelete(request, pk):
    prediction = get_object_or_404(Prediction,pk=pk,Patient__user=request.user)
    pat_pk = prediction.Patient.pk
    prediction.delete()
    pred = Prediction.objects.filter(Patient=pat_pk).last()
    last_prediction = pred.heartDisease
    last_prediction_prob = pred.heartDiseaseProb
    patient = patient = get_object_or_404(Patient,pk=pat_pk)
    patient.last_prediction = int(last_prediction)
    patient.last_prediction_prob = last_prediction_prob
    patient.save()
    return redirect('../prediction_list/'+str(pat_pk))

def prediction(request):
    form = PredictionForm()
    hdisease = None
    hdProb = None
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():           
            temp = np.array([[
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
            ]])
            temp_pd = pd.DataFrame(temp,columns=non_proc_labels)
            ohEncoder = joblib.load('aiModels/OHEncoder.pkl')
            transformed_temp = ohEncoder.transform(temp_pd)
            sScaler = joblib.load('aiModels/SScaler.pkl')
            sc_transformed_temp = sScaler.transform(transformed_temp)
            aimod = form.cleaned_data['aiModel']
            if aimod == 0 :
                #xgb_class = joblib.load('aiModels/XGBClassifier.pkl')
                mlp_classifier = joblib.load('aiModels/MLPClassifier.pkl')
                hdisease = mlp_classifier.predict(sc_transformed_temp)[0]
                hdProb = mlp_classifier.predict_proba(sc_transformed_temp)[0][1]*100
            else:
                svClassifier = joblib.load('aiModels/SVClassifier.pkl')
                hdisease = svClassifier.predict(sc_transformed_temp)[0]
                hdProb = svClassifier.predict_proba(sc_transformed_temp)[0][1]*100
            hdProb = round(hdProb, 2)
    context = {'form': form,
              'hdisease':hdisease,
              'hdProb':hdProb}
    return render(request, 'prediction.html',context)
