import email
from http.client import HTTPResponse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import response
from sqlalchemy import distinct
#from matplotlib.style import context
from .filters import *
from .models import *
#from projectTesis.apps.app1.models import Patient
from .forms import *
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.utils.translation import gettext as _
import numpy as np
import pandas as pd
import joblib
import datetime

#Reload Ai Model
reloadModel = joblib.load('aiModels/XGBClassifier.pkl')
#Reload OneHotEncoder
ohEncoder = joblib.load('aiModels/OHEncoder.pkl')
#Reload StandardScaler
sScaler = joblib.load('aiModels/SScaler.pkl')
#Reload Soft Voting Classifier
svClassifier = joblib.load('aiModels/SVClassifier.pkl')


non_proc_labels = ['Age', 'Sex', 'ChestPainType', 'RestingBP', 'Cholesterol', 'FastingBS',
       'RestingECG', 'MaxHR', 'ExerciseAngina', 'Oldpeak', 'ST_Slope']
proc_labels = ['Sex_F', 'Sex_M',
       'ChestPainType_ASY','ChestPainType_ATA','ChestPainType_NAP','ChestPainType_TA', 'RestingECG_LVH',
       'RestingECG_Normal', 'RestingECG_ST',
       'ExerciseAngina_N','ExerciseAngina_Y', 
       'ST_Slope_Down','ST_Slope_Flat', 'ST_Slope_Up',
       'Age', 'RestingBP', 'Cholesterol',
       'FastingBS', 'MaxHR', 'Oldpeak']

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
                messages.success(request,_('Account was created for ')+user)
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
                messages.info(request, _('Username or Password is incorrect'))
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
            messages.success(request,_('Account was updated for ')+user)
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


def patientList(request):
    user = request.user
    patients = Patient.objects.filter(user=user)
    filter = PatientFilter(request.GET,queryset=patients)
    patients = filter.qs#.distinct() 
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
    return render(request, 'patient_detail.html',context)

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

########Prediction

def predictionList(request, pk):
    patient = get_object_or_404(Patient,pk=pk,user=request.user)
    #user = request.user
    predictions = Prediction.objects.filter(Patient=patient).order_by('-pk')
    filter = PredictionFilter(request.GET,queryset=predictions)
    predictions = filter.qs
    context = {'pred_list':predictions,'filter':filter,'patient':patient}
    return render(request,"prediction_list.html",context)

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
            transformed_temp = ohEncoder.transform(temp_pd)
            sc_transformed_temp = sScaler.transform(transformed_temp)
            aimod = form.cleaned_data['aiModel']
            if aimod == 0 :
                hdisease = reloadModel.predict(sc_transformed_temp)[0]
                hdProb = reloadModel.predict_proba(sc_transformed_temp)[0][1]*100
            else:
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

def predictionDetail(request, pk):
    prediction = get_object_or_404(Prediction,pk=pk,Patient__user=request.user)
    form = DetailPredictionForm(instance=prediction)
    context = {"prediction":prediction,"form":form,"patient":prediction.Patient}
    return render(request, 'prediction_detail.html',context)

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
            transformed_temp = ohEncoder.transform(temp_pd)
            sc_transformed_temp = sScaler.transform(transformed_temp)
            aimod = form.cleaned_data['aiModel']
            if aimod == 0 :
                hdisease = reloadModel.predict(sc_transformed_temp)[0]
                hdProb = reloadModel.predict_proba(sc_transformed_temp)[0][1]*100
            else:
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
    context = {"prediction":prediction,"form":form}
    return render(request, 'prediction_edit.html',context)

def predictionDelete(request, pk):
    prediction = get_object_or_404(Prediction,pk=pk,Patient__user=request.user)
    pat_pk = prediction.Patient.pk
    prediction.delete()
    return redirect('../prediction_list/'+str(pat_pk))

def featureImportance(request):
    f_importances = reloadModel.feature_importances_*100
    labels = proc_labels
    context = {'f_importances':f_importances,
                'labels':labels}
    return render(request, 'feature_importance.html',context)

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
            transformed_temp = ohEncoder.transform(temp_pd)
            sc_transformed_temp = sScaler.transform(transformed_temp)
            aimod = form.cleaned_data['aiModel']
            if aimod == 0 :
                hdisease = reloadModel.predict(sc_transformed_temp)[0]
                hdProb = reloadModel.predict_proba(sc_transformed_temp)[0][1]*100
            else:
                hdisease = svClassifier.predict(sc_transformed_temp)[0]
                hdProb = svClassifier.predict_proba(sc_transformed_temp)[0][1]*100
            hdProb = round(hdProb, 2)
    context = {'form': form,
              'hdisease':hdisease,
              'hdProb':hdProb}
    return render(request, 'prediction.html',context)


def addPredictionToTrain(request, pk):
    user = request.user 
    pred = get_object_or_404(Prediction,pk=pk,Patient__user=user)
    if request.method == 'GET':
        try:
            pred_to_train = PredictionToTrain.objects.get(prediction=pred)
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

def predictionToTrainList(request):
    user = request.user
    pred_list = PredictionToTrain.objects.filter(
        prediction__Patient__user=user,
        was_used = False
    ).order_by('-pk')
    context = {'pred_list': pred_list}
    return render(request,'prediction_to_train_list.html',context)

def predictionToTrainDetail(request, pk):
    user = request.user 
    prediction = get_object_or_404(PredictionToTrain,pk=pk,prediction__Patient__user=user)
    patient = prediction.prediction.Patient
    form = DetailPredictionToTrainForm(instance=prediction)
    context = {"prediction":prediction,"form":form,"patient":patient}
    return render(request, 'prediction_to_train_detail.html',context)

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

def predictionToTrainDelete(request, pk):
    user = request.user 
    prediction = get_object_or_404(PredictionToTrain,pk=pk,prediction__Patient__user=user)
    prediction.delete()
    return redirect('prediction_to_train_list')
"""
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
        tempy = np.array([[prediction.heartDisease]]) 
        tempx_pd = pd.DataFrame(tempx,columns=non_proc_labels)
        transformed_tempx = ohEncoder.transform(tempx_pd)
        sc_transformed_tempx = sScaler.transform(transformed_tempx) 
        aimod = prediction.aiModel
        if aimod == 0:
            reloadModel = joblib.load('aiModels/XGBClassifier.pkl')
            reloadModel.fit(sc_transformed_tempx,tempy)
        else:
            svClassifier = joblib.load('aiModels/SVClassifier.pkl')
            svClassifier.fit(sc_transformed_tempx,tempy)
    return render(request, 'prediction_to_train_detail.html',context)
"""