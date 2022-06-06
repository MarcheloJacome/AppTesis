"""
Django settings for projectTesis project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
from django.utils.translation import gettext_lazy as _
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '45c+k*(=b5)e_2eozcld$h7pfcx)3v1n@g$35(tbimo&md5%bk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#DEBUG = False

ALLOWED_HOSTS = ['tesis-deployment-appservice.azurewebsites.net','127.0.0.1']
CSRF_TRUSTED_ORIGINS = ['http://tesis-deployment-appservice.azurewebsites.net','https://www.tesis-deployment-appservice.azurewebsites.net']
#CSRF_TRUSTED_ORIGINS = ['http://tesis-deployment-appservice.azurewebsites.net','https://www.tesis-deployment-appservice.azurewebsites.net','tesis-deployment-appservice.azurewebsites.net']
# Application definition

INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'crispy_bootstrap5',
    'django_filters',
    'apps.app1',
    'apps.app_patient',
    'apps.app_prediction',
    'apps.app_training_prediction',
    'apps.app1.templatetags',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'projectTesis.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

WSGI_APPLICATION = 'projectTesis.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

#Must add credential as environmental variables and read their values in Python
"""
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'django_sqlserver_1',
        'USER': 'sa',
        'PASSWORD': '123456',
        'HOST': 'DESKTOP-5NCIOMV',
        'PORT': '',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server'
        },
    }
}
"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tesisDeployDB',
        'USER': 'adminPostgreeTesis@tesis-deployment-server',
        #'PASSWORD': 'Sitemanage2022',
        'PASSWORD': os.getenv("DB_PASSWORD"),
        'HOST': 'tesis-deployment-server.postgres.database.azure.com',
        'PORT': '5432',
        "OPTIONS": {
            "sslmode" : "require",
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/


LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


LOCALE_PATHS = (BASE_DIR + 'locale/', )
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = BASE_DIR + '/' + 'staticfiles'
STATICFILES_DIRS = [
   os.path.join(BASE_DIR, 'static')
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
#EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
#EMAIL_HOST_PASSWORD = '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'
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
#DEFAULT_FROM_EMAIL = 'tesis4810@outlook.com'
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")