import os
from pathlib import Path
from pymongo import MongoClient
from decouple import config, Config, RepositoryEnv

BASE_DIR = Path(__file__).resolve().parent.parent

env_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
config = Config(RepositoryEnv(env_file)) if os.path.exists(env_file) else config

SECRET_KEY = config('SECRET_KEY_DJANGO')

SITE = config('SITE')
SITE_URL = f'https://{SITE}'
SITE_URL_API = config('SITE_URL_API')

DEBUG = config('DEBUG_DJANGO', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS_DJANGO', cast=lambda v: [s.strip() for s in v.split(',')])

CSRF_TRUSTED_ORIGINS = [
    f"{SITE_URL}",
    f"{SITE_URL_API}"
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework",
    "payme",
    "drf_spectacular",
    "corsheaders",

    "payment",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

CORS_ALLOWED_ORIGINS = [
    f"{SITE_URL}",
    f"{SITE_URL_API}"
]

ROOT_URLCONF = "core.urls"

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
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
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

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Tashkent"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

PAYME_ID = config('PAYME_ID')
PAYME_KEY = config('PAYME_KEY')
PAYME_KEY_TEST = config('PAYME_KEY_TEST')
PAYME_ACCOUNT_FIELD = config('PAYME_ACCOUNT_FIELD')
PAYME_AMOUNT_FIELD = config('PAYME_AMOUNT_FIELD')
PAYME_ACCOUNT_MODEL = "payment.models.Order"
PAYME_ONE_TIME_PAYMENT = True

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'SpeakEz payment API',
    'DESCRIPTION': 'SpeakEz payment API',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False
}

MONGO_URI = config('MONGO_URI')
client = MongoClient(MONGO_URI)
db = client["chatgpt_telegram_bot"]
users_collection = db["user"]
