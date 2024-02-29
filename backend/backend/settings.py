"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path
from dotenv import load_dotenv
import datetime

load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition1

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "sitedb.apps.SitedbConfig",  # Site Info etc
    "users.apps.UsersConfig",  # AUTH USER API
    "profiles.apps.ProfilesConfig",  # User Profiles API
    "telegram.apps.TelegramConfig",  # Integrate TG BOT
    "DB.apps.DbConfig",  # Database
    "order.apps.OrderConfig",  # Order API
    "API.apps.ApiConfig",  # Product API
    "reviews.apps.ReviewsConfig",  # Reviews API
    "django_filters",
    "allauth",  # work with users
    "allauth.account",
    "allauth.socialaccount",
    "rest_framework",
    "rest_framework.authtoken",
    "rest_framework_swagger",  # swagger and docs
    "drf_yasg",
    "smsru",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
            os.path.join(BASE_DIR, "users/templates"),
            os.path.join(BASE_DIR, "DB/templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


"""
БАЗА ДАННЫХ
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("POSTGRES_HOST"),
        "PORT": os.getenv("POSTGRES_PORT"),
    }
}
"""
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "ru"

TIME_ZONE = "Asia/Yekaterinburg"

USE_I18N = True

USE_TZ = True


"""
STATIC SETTINGS
"""
STATIC_URL = "static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]


"""
MEDIA SETTINGS
"""
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


"""
SITE_ID 
"""
SITE_ID = 1


"""
REST FRAMEWORK
"""
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}


"""
JWT TOKEN
"""
JWT_AUTH = {
    "JWT_EXPIRATION_DELTA": datetime.timedelta(
        hours=5
    ),  # Срок действия Access Token на 5 часов
    "JWT_REFRESH_EXPIRATION_DELTA": datetime.timedelta(
        days=7
    ),  # Срок действия Refresh Token на 7 дней
    "JWT_ALLOW_REFRESH": True,  # Разрешить обновление токена
}


"""
CUSTOM MODEL USER
"""
AUTH_USER_MODEL = "users.CustomUser"


"""
LOGGING
"""
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "file_format": {
            "format": "[%(asctime)s] %(levelname)s|%(module)s: %(message)s",
            "datefmt": "%d.%m.%Y %H:%M:%S",
        },
        "error_format": {
            "format": "[%(asctime)s - %(levelname)s] %(message)s, путь: %(pathname)s, строка: %(lineno)d",
            "datefmt": "%d.%m.%Y %H:%M:%S",
        },
        "security_error": {
            "format": "[%(asctime)s] - [%(levelname)s] - [%(module)s] - %(message)s",
            "datefmt": "%d/%m/%Y %H:%M:%S",
        },
    },
    "handlers": {
        "errors": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(BASE_DIR, "logs/errors.log"),
            "maxBytes": 1024 * 1024 * 5,
            "backupCount": 5,
            "formatter": "error_format",
            "level": "ERROR",
        },
        "security": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(BASE_DIR, "logs/security.log"),
            "maxBytes": 1024 * 1024 * 5,
            "backupCount": 5,
            "formatter": "security_error",
            "level": "INFO",
        },
    },
    "loggers": {
        "django.request": {"handlers": ["errors"], "level": "ERROR", "propagate": True},
        "django.security": {
            "handlers": ["security"],
            "level": "INFO",
            "propagate": True,
        },
    },
}


"""
MAIL SETTINGS
"""
# if DEBUG:
#     EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# else:
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.yandex.ru"
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


"""
REDIS SETTINGS
"""
REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")
REDIS_DB = os.getenv("REDIS_DB")


"""
CELERY SETTINGS
"""
CELERY_BROKER_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True


"""
SMS SETTINGS
"""
SMS_RU = {
    "API_ID": os.getenv("SMS_RU_API_ID"),
    "FROM": os.getenv("SMSRU_FROM"),
}
