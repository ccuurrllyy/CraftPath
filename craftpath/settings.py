"""
Django settings for craftpath project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
import json
from craftpath.tools import get_secret

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

try:
    with open('%s/%s' % (BASE_DIR, 'secrets.json')) as f:
        SECRETS = json.loads(f.read())
except IOError:
    SECRETS = dict()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

SERVER_TYPE = get_secret('SERVER_TYPE', SECRETS, 'LOCAL')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5px#-d^gx=ufx9a4m!02mdez_=&7!#8riq^^eomizd(#s_1lyb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = get_secret('DEBUG', SECRETS, False)

if DEBUG:
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = []



# Application definition

INSTALLED_APPS = [
    'blog.apps.BlogConfig',
    'users.apps.UsersConfig',
    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'django_email_verification',
    'rest_framework',
    'import_export',
    'widget_tweaks',
    'mapwidgets',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'craftpath.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'craftpath.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
        'default': {
            # 'ENGINE': 'django.contrib.gis.db.backends.mysql',
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': get_secret('DATABASE_NAME', SECRETS),
            'USER': get_secret('DATABASE_USER', SECRETS),
            'PASSWORD': get_secret('DATABASE_PASSWORD', SECRETS),
            'HOST': get_secret('DATABASE_HOST', SECRETS),
            'PORT': '',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIR = [
    os.path.join(BASE_DIR, 'static')
]

MEDIA_URL = '/images/'
CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'blog-main'
LOGIN_URL = 'login'

GOOGLE_GEOCODE_API_KEY = get_secret('GOOGLE_GEOCODE_API_KEY', SECRETS)

MAP_WIDGETS = {
    "GooglePointFieldWidget": (
        ("zoom", 15),
        ("mapCenterLocationName", "Abu Dhabi"),
        ("GooglePlaceAutocompleteOptions", {'componentRestrictions': {'country': 'ae'}}),
        ("markerFitZoom", 12),
    ),
    "GOOGLE_MAP_API_KEY": GOOGLE_GEOCODE_API_KEY
}

EMAIL_ACTIVE_FIELD = 'is_active'
EMAIL_SERVER = get_secret('EMAIL_SERVER', SECRETS, "smtp.gmail.com")
EMAIL_PORT = 587
EMAIL_FROM_ADDRESS = get_secret('FROM_EMAIL', SECRETS, 'noreply@example.com')
EMAIL_ADDRESS = get_secret('EMAIL_ADDRESS', SECRETS, 'noreply@example.com')
EMAIL_PASSWORD = get_secret('EMAIL_PASSWORD', SECRETS,  '')
EMAIL_MAIL_SUBJECT = 'CraftPath | Confirm your email'
EMAIL_MAIL_HTML = os.path.join(BASE_DIR, 'users/templates/users/confirmation_email.html')
EMAIL_MAIL_PLAIN = os.path.join(BASE_DIR, 'users/templates/users/confirmation_email_plain.txt')
EMAIL_PAGE_TEMPLATE = os.path.join(BASE_DIR, 'users/templates/users/email_confirmation_page.html')
EMAIL_PAGE_DOMAIN = get_secret('PAGE_DOMAIN', SECRETS, 'http://127.0.0.1:8000')


#these dont work!
#EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
#EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')