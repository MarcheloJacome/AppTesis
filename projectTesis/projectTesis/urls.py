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
from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
#from django.conf.urls import url
from apps.app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('prediction/', views.prediction, name='Prediction'),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('edit_user/', views.editUser, name="edit_user"),
    path('change_user_pass/', views.changeUserPass, name="change_user_pass"),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name="password_reset_complete"),
    path('patient_list/', views.patientList, name="patient_list"),
    path('patient_create/', views.patientCreate, name="patient_create"),
    path('patient_detail/<int:pk>', views.patientDetail, name="patient_detail"),
    path('patient_edit/<int:pk>', views.patientEdit, name="patient_edit"),
    path('patient_delete/<int:pk>', views.patientDelete, name="patient_delete"),
    path('prediction_list/<int:pk>', views.predictionList, name="prediction_list"),
    path('prediction_create/<int:pk>', views.predictionCreate, name="prediction_create"),
    path('prediction_detail/<int:pk>', views.predictionDetail, name="prediction_detail"),
    path('prediction_edit/<int:pk>', views.predictionEdit, name="prediction_edit"),
    path('prediction_delete/<int:pk>', views.predictionDelete, name="prediction_delete"),
    path('feature_importance/', views.featureImportance, name="feature_importance"),
    #re_path('predictHD', views.predictHD, name='predictHD'),
]
