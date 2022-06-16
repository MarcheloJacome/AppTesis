from django.shortcuts import render, redirect
from .forms import CreateUserForm, EditUserForm, DataAnalyticsHistForm,DataAnalyticsBarsForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required
from apps.app_training_prediction.models import PredictionToTrain
import pandas as pd
import numpy as np
import joblib
import json
from plotly.offline import plot
import plotly.express as px



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

    feat_dict = {}
    for i in range(len(f_importances)):
        feat_dict[proc_labels[i]] = f_importances[i]
    feat_dict
    sorted_feat_dict = {k: v for k, v in sorted(feat_dict.items(), key=lambda item: item[1])}
    sort_f_importances = []
    labels = []
    for key in feat_dict:
        if feat_dict[key] > 0:
            sort_f_importances += [feat_dict[key]]
            labels += [key]
    main_label = _('Feature Importance %')
    context = {'f_importances':sort_f_importances,
                'labels':labels,
                'main_label':main_label}
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

@login_required(login_url="/login")
def data_analytics(request):
    qs = PredictionToTrain.objects.all()
    predictions_data = [
        {
           _('Age') :  i.age,
           _('Sex') :  i.sex,
           _('ChestPainType') :  i.chestPainType,
           _('RestingBP') :  i.restingBP,
           _('Cholesterol') :  i.cholesterol,
           _('FastingBS') :  i.fastingBS,
           _('RestingECG') :  i.restingECG,
           _('MaxHR') :  i.maxHR,
           _('ExerciseAngina') :  i.exerciseAngina,
           _('Oldpeak') :  i.oldpeak,
           _('ST_Slope') :  i.sT_Slope,
           _('HeartDisease') :  i.heartDisease,
        } for i in qs
    ]
    df = pd.DataFrame(predictions_data)
    output_hist = request.GET.get('output')
    x_label_hist = request.GET.get('x_label')
    hue_hist = request.GET.get('hue')
    hist_output = 0
    hist_x = _('Age')
    hist_hue = _('Sex')
    if output_hist:
        hist_output = output_hist
    if x_label_hist:
        hist_x = x_label_hist
    if hue_hist:
        hist_hue = hue_hist
    df_hist = df[df[_('HeartDisease')]==int(hist_output)]
    if int(hist_output) == 3:
        df_hist = df
    fig_hist = px.histogram(df_hist, x=hist_x,color=hist_hue,
                         marginal="rug", hover_data=df.columns).update_layout(
                             yaxis_title=_('Heart Disease Output (Total)'),
                             height=700
                         )
    gantt_plot_hist = plot(fig_hist, output_type="div")

    output_bar = request.GET.get('output_bar')
    x_label_bar = request.GET.get('x_label_bar')
    bar_output = 0
    bar_x = _('Age')
    if output_bar:
        bar_output = output_bar
    if x_label_bar:
        bar_x = x_label_bar
    df_bar = df[df[_('HeartDisease')]==int(bar_output)]
    if int(bar_output) == 3:
        df_bar = df
    fig_bar = px.histogram(df_bar, x=bar_x,
                         marginal="rug", hover_data=df.columns).update_layout(
                             yaxis_title=_('Heart Disease Output (Total)'),
                             height=700
                         )
    gantt_plot_bar = plot(fig_bar, output_type="div")

    context = {'plot_div_hist': gantt_plot_hist,
               'plot_div_bar': gantt_plot_bar,
               'form_bar':DataAnalyticsBarsForm(request.GET),
               'form_hist':DataAnalyticsHistForm(request.GET)}
    return render(request, 'data_analytics.html',context)