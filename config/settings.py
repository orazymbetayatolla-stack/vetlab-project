from pathlib import Path
from django.utils.translation import gettext_lazy as _
from django.contrib.messages import constants as messages

# =============================
# BASE
# =============================

BASE_DIR = Path(__file__).resolve().parent.parent


# =============================
# SECURITY
# =============================

SECRET_KEY = 'django-insecure-g(+#a9es2)s!c=u9qtvfai&q+a9opc%9vyno51w(-nf5d-vqb!'

DEBUG = True

ALLOWED_HOSTS = ['*']


# =============================
# APPLICATIONS
# =============================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'main',
]


# =============================
# MIDDLEWARE
# =============================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.locale.LocaleMiddleware',  # ← ВАЖНО тут

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]





# =============================
# URLS / TEMPLATES
# =============================

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # используем templates внутри app
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

WSGI_APPLICATION = 'config.wsgi.application'


# =============================
# DATABASE
# =============================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# =============================
# PASSWORDS
# =============================

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


# =============================
# 🌍 INTERNATIONALIZATION
# =============================

LANGUAGE_CODE = 'ru'

LANGUAGES = [
    ('ru', 'Русский'),
    ('kk', 'Қазақша'),
    ('en', 'English'),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

TIME_ZONE = 'Asia/Almaty'

USE_I18N = True
USE_L10N = True
USE_TZ = True


# =============================
# STATIC / MEDIA
# =============================

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# =============================
# DEFAULTS
# =============================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LANGUAGE_COOKIE_NAME = 'django_language'
LANGUAGE_COOKIE_AGE = 60 * 60 * 24 * 365  # 1 год
LANGUAGE_COOKIE_PATH = '/'

