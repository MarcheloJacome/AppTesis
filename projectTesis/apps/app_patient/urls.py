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
    path('patient_list/', patientList, name="patient_list"),
    path('patient_create/', patientCreate, name="patient_create"),
    path('patient_detail/<int:pk>', patientDetail, name="patient_detail"),
    path('patient_edit/<int:pk>', patientEdit, name="patient_edit"),
    path('patient_delete/<int:pk>', patientDelete, name="patient_delete"),
]
