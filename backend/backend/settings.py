import os
from pathlib import Path
from dotenv import load_dotenv
from celery.schedules import crontab, timedelta

from .config import SQLITE, POSTGRES

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*", "localhost"]

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]
CORS_ALLOWED_ORIGIN_REGEXES = [
    "http://localhost:3000",
]

CORS_ALLOW_HEADERS = [
    "accept",
    "referer",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-sessionid",
    "x-requested-with",
    "access",
    "refresh",
]

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

CSRF_TRUSTED_ORIGINS = [os.getenv("CSRF_TRUSTED_ORIGINS")]

INTERNAL_IPS = [
    "127.0.0.1",
]

# Application definition1

INSTALLED_APPS = [
    "jazzmin.apps.JazzminConfig",  # ADMIN
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",  # CORS
    "sitedb.apps.SitedbConfig",  # Site Info etc
    "users.apps.UsersConfig",  # AUTH USER API
    "profiles.apps.ProfilesConfig",  # User Profiles API
    "telegram.apps.TelegramConfig",  # Integrate TG BOT
    "DB.apps.DbConfig",  # Database
    "order.apps.OrderConfig",  # Order API
    "API.apps.ApiConfig",  # Product API
    "reviews.apps.ReviewsConfig",  # Reviews API
    "vacancy.apps.VacancyConfig",  # Vacancy API
    "django_filters",  # Filters
    "colorfield",  # color field
    "rest_framework",  # API
    "rest_framework.authtoken",  # Auth
    "rest_framework_swagger",  # swagger and docs
    "drf_yasg",  # swagger and docs
    "smsru",  # SMS
    "django_ckeditor_5",  # ckeditor
    "image_uploader_widget",  # Image Widget
    "debug_toolbar",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

X_FRAME_OPTIONS = "SAMEORIGIN"


ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
            os.path.join(BASE_DIR, "users/templates"),
            os.path.join(BASE_DIR, "DB/templates"),
            os.path.join(BASE_DIR, "sitedb/templates"),
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
DATA BASE
"""
# POSTGRESQL DATABASE Check ENV
# DATABASES = POSTGRES

# Uncomment if you want to use sqlite
DATABASES = SQLITE


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
]


LANGUAGE_CODE = "ru"

TIME_ZONE = "Asia/Yekaterinburg"

USE_I18N = True

USE_TZ = True


"""
STATIC SETTINGS
"""


STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

"""
MEDIA SETTINGS
"""
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

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
    # # КАСТОМНЫЕ КЛАССЫ
    # "DEFAULT_THROTTLE_CLASSES": [
    #     "API.Throttling.ThrottlingAnonUsers.UserReviewsThrottle",
    #     "API.Throttling.ThrottlingAnonUsers.SearchThrottle",
    #     "API.Throttling.ThrottlingAnonUsers.FeedbackThrottle",
    #     "API.Throttling.ThrottlingAuthUsers.ChangeInfoThrottle",
    #     "API.Throttling.ThrottlingAuthUsers.ChangePasswordThrottle",
    #     "API.Throttling.ThrottlingAuthUsers.UserReviewsThrottle",
    # ],
    # # КОЛВО ЗАПРОСОВ НА КАЖДЫЙ СКОП
    # "DEFAULT_THROTTLE_RATES": {
    #     "anon": "10/min",
    #     "user": "5/day",
    #     "user_reviews": "3/day",
    #     "search": "30/min",
    #     "change_info": "10/day",
    #     "change_password": "15/day",
    #     "user_reviews": "3/day",
    #     "feedback": "20/day",
    # },
}


"""
JWT TOKEN
"""

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=int(os.getenv("ACCESS_TOKEN_LIFETIME"))),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=int(os.getenv("REFRESH_TOKEN_LIFETIME"))),
    "ROTATE_REFRESH_TOKENS": True,
}

"""
CUSTOM MODEL USER
"""
AUTH_USER_MODEL = "users.CustomUser"


"""
LOGGING
"""
from .config import SET_LOGGING

LOGGING = SET_LOGGING

"""
MAIL SETTINGS
"""

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
REDIS_HOST = os.getenv("REDIS_HOST", "127.0.0.1")
REDIS_PORT = os.getenv("REDIS_PORT")
REDIS_DB = os.getenv("REDIS_DB")


"""
CELERY SETTINGS
"""

CELERY_BROKER_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"
CELERY_RESULT_BACKEND = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"


CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = TIME_ZONE

"""
SMS SETTINGS
"""
from .config import SMS_SETTINGS


SMS_RU = SMS_SETTINGS


"""
Yookassa
"""
YOOKASSA_ACCOUNT_ID = os.getenv("YOOKASSA_ACCOUNT_ID")
YOOKASSA_SECRET = os.getenv("YOOKASSA_SECRET")

# ADMIN SETTINGS
from .config import JAZZ_SETTINGS

JAZZMIN_SETTINGS = JAZZ_SETTINGS


# UI ADMIN
from .config import UI_SETTINGS

JAZZMIN_UI_TWEAKS = UI_SETTINGS

from .config import CKEDITOR_5_CONFIGS_SETTINGS

CKEDITOR_5_CONFIGS = CKEDITOR_5_CONFIGS_SETTINGS

CKEDITOR_5_FILE_STORAGE = "backend.config.ckreditor.storage.CustomStorage"


# CELERY PEREODIC TASKS

CELERY_BEAT_SCHEDULE = {
    "check_sertificate": {
        "task": "sitedb.tasks.check_sertificate",
        "schedule": crontab(hour=8, minute=0),
    },
}


SITE_URL = os.getenv("SITE_URL")

API_VERSION = os.getenv("API_VERSION")
