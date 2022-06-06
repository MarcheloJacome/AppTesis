"""projectTesis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *
urlpatterns = [
    path('prediction_to_train_add/<int:pk>', addPredictionToTrain, name="prediction_to_train_add"),
    path('prediction_to_train_list/', predictionToTrainList, name="prediction_to_train_list"),
    path('prediction_to_train_detail/<int:pk>', predictionToTrainDetail, name="prediction_to_train_detail"),
    path('prediction_to_train_edit/<int:pk>', predictionToTrainEdit, name="prediction_to_train_edit"),
    path('prediction_to_train_delete/<int:pk>', predictionToTrainDelete, name="prediction_to_train_delete"),
    path('prediction_to_train_confirm/<int:pk>', predictionToTrainConfirm, name="prediction_to_train_confirm"),
]
