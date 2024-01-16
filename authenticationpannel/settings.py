"""
Django settings for authenticationpannel project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-uwz$jar@@8afs+ghw6+zm!9h_by1%^w%o&9&#i-2(4zi_+!b&$"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["codex-auth.azurewebsites.net", "localhost"]

# Application definition
INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    "app",
    "api",
    "rest_framework",  # Django REST Framework
    "crispy_bootstrap5",  # Django Crispy Bootstrap5
    "crispy_forms",  # Django Crispy Forms
    "oauth2_provider",  # Django OAuth Toolkit
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "oauth2_provider.middleware.OAuth2TokenMiddleware",
]

AUTHENTICATION_BACKENDS = ("oauth2_provider.backends.OAuth2Backend", "django.contrib.auth.backends.ModelBackend")

CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = ["https://codex-auth.azurewebsites.net", "http://localhost:3000"]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = ["GET", "POST", "PUT"]

ROOT_URLCONF = "authenticationpannel.urls"
MEDIA_URL = "/media/"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.csrf",
            ],
        },
    },
]

WSGI_APPLICATION = "authenticationpannel.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "CodexAdmin",
        "PASSWORD": "OAuth321AHDJ",
        "HOST": "codex-storage.postgres.database.azure.com",
        "PORT": "5432",
        "OPTIONS": {"sslmode": "require", "sslrootcert": "cert/DigiCertGlobalRootCA.crt.pem"},
    }
}

# Email Settings
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "authcodex@gmail.com"
EMAIL_HOST_PASSWORD = "rusx ifkc zzdr ebwb"

AUTH_USER_MODEL = "app.UserProfile"

OAUTH2_PROVIDER = {"SCOPES": {"read": "read_scope", "write": "write_scope", "groups": "Access to your groups"}}
REST_FRAMEWORK = {"DEFAULT_AUTHENTICATION_CLASSES": ("oauth2_provider.contrib.rest_framework.OAuth2Authentication",)}

LOGIN_URL = "app:login"
LOGIN_REDIRECT_URL = "app:profile"

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

PROJECT_ROOT = os.path.normpath(os.path.dirname(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, "static")
STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
