from django.shortcuts import render, redirect
from .forms import CreateUserForm, EditUserForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required
import pandas as pd
import numpy as np
import joblib
import json



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
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, _('Username or Password is incorrect'))
        context = {}
        return render(request,'login.html',context)

@login_required(login_url="/login")
def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url="/login")
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

@login_required(login_url="/login")
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


def featureImportance(request):
    proc_labels = [_('Sex_F'), _('Sex_M'),
       _('ChestPainType_ASY'),_('ChestPainType_ATA'),_('ChestPainType_NAP'),_('ChestPainType_TA'), _('RestingECG_LVH'),
       _('RestingECG_Normal'), _('RestingECG_ST'),
       _('ExerciseAngina_N'),_('ExerciseAngina_Y'), 
       _('ST_Slope_Down'),_('ST_Slope_Flat'), _('ST_Slope_Up'),
       _('Age'), _('RestingBP'), _('Cholesterol'),
       _('FastingBS'), _('MaxHR'), _('Oldpeak')]
    xgb_class = joblib.load('aiModels/XGBClassifier.pkl')
    f_importances = np.round(xgb_class.feature_importances_*100,2)
    labels = proc_labels
    context = {'f_importances':f_importances,
                'labels':labels}
    return render(request, 'feature_importance.html',context)

def aboutAIModels(request):
    return render(request, 'about_ai_models.html')

def aboutDataset(request):
    non_proc_lab = ['Age', 'Sex', 'ChestPainType', 'RestingBP', 'Cholesterol', 'FastingBS',
        'RestingECG', 'MaxHR', 'ExerciseAngina', 'Oldpeak', 'ST_Slope', 'HeartDisease']
    proc_labels = ['Sex_F', 'Sex_M',
        'ChestPainType_ASY','ChestPainType_ATA','ChestPainType_NAP','ChestPainType_TA', 'RestingECG_LVH',
        'RestingECG_Normal', 'RestingECG_ST',
        'ExerciseAngina_N','ExerciseAngina_Y', 
        'ST_Slope_Down','ST_Slope_Flat', 'ST_Slope_Up',
        'Age', 'RestingBP', 'Cholesterol',
        'FastingBS', 'MaxHR', 'Oldpeak',
        'HeartDisease']
    df = pd.read_csv("apps/app1/static/app1/Data/heart.csv")
    df = df.head(20)
    json_rec = df.reset_index().to_json(orient='records')
    arr = []
    arr = json.loads(json_rec)
    ohEncoderOriginal = joblib.load('aiModels/OHEncoderOriginal.pkl')
    transformed_df = ohEncoderOriginal.transform(df)
    encoded_pd = pd.DataFrame(transformed_df, columns=proc_labels)
    json_rec_encoded = encoded_pd.reset_index().to_json(orient='records')
    arr_encoded = []
    arr_encoded = json.loads(json_rec_encoded)
    context = {"arr":arr,
              "non_proc_lab":non_proc_lab,
              "arr_encoded":arr_encoded,
              "proc_labels":proc_labels}
    return render(request, 'about_dataset.html',context)
