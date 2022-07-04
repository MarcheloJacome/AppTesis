from django.shortcuts import render, redirect, get_object_or_404
from .filters import PredictionToTrainFilter
from .models import PredictionToTrain, Prediction
from .forms import *
from django.contrib import messages
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required
import numpy as np
import pandas as pd
import joblib
import datetime


non_proc_labels = ['Age', 'Sex', 'ChestPainType', 'RestingBP', 'Cholesterol', 'FastingBS',
       'RestingECG', 'MaxHR', 'ExerciseAngina', 'Oldpeak', 'ST_Slope']

@login_required(login_url="/login")
def addPredictionToTrain(request, pk):
    user = request.user 
    pred = get_object_or_404(Prediction,pk=pk,Patient__user=user)
    if request.method == 'GET':
        try:
            pred_to_train = PredictionToTrain.objects.get(prediction=pred)
            if pred_to_train is not None:
                messages.add_message(request, messages.ERROR,
                        _('Could not add prediction. It was already used to train the model!'))
        except PredictionToTrain.DoesNotExist:
            PredictionToTrain.objects.create(
                date_created = pred.date_created,
                age = pred.age,
                sex = pred.sex,
                chestPainType = pred.chestPainType,
                restingBP = pred.restingBP,
                cholesterol = pred.cholesterol,
                fastingBS = pred.fastingBS,
                restingECG = pred.restingECG,
                maxHR = pred.maxHR,
                exerciseAngina = pred.exerciseAngina,
                oldpeak = pred.oldpeak,
                sT_Slope = pred.sT_Slope,
                heartDisease = pred.heartDisease,
                aiModel = pred.aiModel,
                prediction = pred,
                was_used = False
            )
        return redirect('prediction_to_train_list')

@login_required(login_url="/login")
def predictionToTrainList(request):
    ##############Delete later
    """
    data = pd.read_csv("apps/app1/static/app1/Data/heart_updated.csv")
    for i in range(len(data)):
        new_Pred =PredictionToTrain.objects.create(
            date_created = datetime.date.today(),
            age = data.iloc[i][0],
            sex = data.iloc[i][1],
            chestPainType = data.iloc[i][2],
            restingBP = data.iloc[i][3],
            cholesterol = data.iloc[i][4],
            fastingBS = data.iloc[i][5],
            restingECG = data.iloc[i][6],
            maxHR = data.iloc[i][7],
            exerciseAngina = data.iloc[i][8],
            oldpeak = data.iloc[i][9],
            sT_Slope = data.iloc[i][10],
            heartDisease = data.iloc[i][11],
            aiModel = 0,
            prediction = None,
            was_used = True
        )
        print(new_Pred)
    """
    ##############Delete later
    user = request.user
    pred_list = PredictionToTrain.objects.filter(
        prediction__Patient__user=user,
        was_used = False
    ).order_by('-pk')
    filter = PredictionToTrainFilter(request.GET,queryset=pred_list)
    pred_list = filter.qs
    context = {'pred_list': pred_list,'filter':filter}
    return render(request,'prediction_to_train_list.html',context)

@login_required(login_url="/login")
def predictionToTrainDetail(request, pk):
    user = request.user 
    prediction = get_object_or_404(PredictionToTrain,pk=pk,prediction__Patient__user=user)
    patient = prediction.prediction.Patient
    form = DetailPredictionToTrainForm(instance=prediction)
    context = {"prediction":prediction,"form":form,"patient":patient}
    return render(request, 'prediction_to_train_detail.html',context)

@login_required(login_url="/login")
def predictionToTrainEdit(request, pk):
    user = request.user 
    prediction = get_object_or_404(PredictionToTrain,pk=pk,prediction__Patient__user=user)
    patient = prediction.prediction.Patient
    form = EditPredictionToTrainForm(instance=prediction)
    form1 = EditPredictionToTrainForm1(instance=prediction)
    if request.method == 'POST':
        form1 = EditPredictionToTrainForm1(request.POST,instance=prediction)
        if form1.is_valid():
            form1.save()
            return redirect('../prediction_to_train_detail'+'/'+str(prediction.pk))
    context = {"prediction":prediction,"form":form,"form1":form1,"patient":patient}
    return render(request, 'prediction_to_train_edit.html',context)

@login_required(login_url="/login")
def predictionToTrainDelete(request, pk):
    user = request.user 
    prediction = get_object_or_404(PredictionToTrain,pk=pk,prediction__Patient__user=user)
    prediction.delete()
    return redirect('prediction_to_train_list')

@login_required(login_url="/login")
def predictionToTrainConfirm(request, pk):
    user = request.user 
    prediction = get_object_or_404(PredictionToTrain,pk=pk,prediction__Patient__user=user)
    patient = prediction.prediction.Patient
    form = DetailPredictionToTrainForm(instance=prediction)   
    if request.method == 'POST':
        tempx = np.array([[
        prediction.age,
        prediction.sex,
        prediction.chestPainType,
        prediction.restingBP,
        prediction.cholesterol,
        prediction.fastingBS,
        prediction.restingECG,
        prediction.maxHR,
        prediction.exerciseAngina,
        prediction.oldpeak,
        prediction.sT_Slope,
        ]])
        tempy = np.array([prediction.heartDisease]) 
        tempx_pd = pd.DataFrame(tempx,columns=non_proc_labels)
        ohEncoder = joblib.load('aiModels/OHEncoder.pkl')
        transformed_tempx = ohEncoder.transform(tempx_pd)
        sScaler = joblib.load('aiModels/SScaler.pkl')
        sc_transformed_tempx = sScaler.transform(transformed_tempx) 
        mlp_classifier = joblib.load('aiModels/MLPClassifier.pkl')
        mlp_classifier.partial_fit(sc_transformed_tempx,tempy)
        joblib.dump(mlp_classifier,'AiModels\MLPClassifier.pkl')
        prediction.was_used = True
        prediction.save()
        return redirect('prediction_to_train_list')
    context = {"patient":patient,"form":form}
    return render(request, 'prediction_to_train_confirm.html',context)
