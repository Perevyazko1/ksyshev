"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#o1gmu7b=&iyyb%xy&ftpl$_)ix1qsfr-ms$m+fj1iw)nivn3)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['985205-ci41159.tmweb.ru',
                 'www.985205-ci41159.tmweb.ru',
                 '127.0.0.1',
                 'localhost',
                 'ci41159.tw1.ru',
                 'www.ci41159.tw1.ru',
                 '192.168.1.188',
                 '192.168.31.196',
                 '192.168.31.194',
                 '684527-cc82345.tmweb.ru',
                 '188.225.47.208'


                 ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'ksyshev.apps.KsyshevConfig',
    'rest_framework',
    'rest_framework.authtoken',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Для работы corsheaders
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_URL = 'static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATICFILES_DIRS = [
    BASE_DIR / "static"
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ADMINS = (
    ('admin', 'a.perevyazko@gmail.com'),
)
# обязательные и необязательные поля регистрации
ACCOUNT_EMAIL_REQUIRED = True  # email является обязательным
ACCOUNT_UNIQUE_EMAIL = True  # email является  уникальным
ACCOUNT_USERNAME_REQUIRED = False  # username необязательный
ACCOUNT_AUTHENTICATION_METHOD = 'email'  # аутентификация будет происходить посредством электронной почты
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'  # верификация почты обязательно

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mail.ru'  # адрес сервера Яндекс-почты для всех один и тот же
EMAIL_PORT = 465  # порт smtp сервера тоже одинаковый
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")  # ваше имя пользователя, например, если ваша почта user@yandex.ru,
# то сюда надо писать user, иными словами, это всё то что идёт до собаки
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")  # пароль от почты
EMAIL_USE_SSL = True  # Яндекс использует ssl, подробнее о том, что это, почитайте в дополнительных источниках,
# но включать его здесь обязательно
SERVER_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'general': {
            'format': '%(asctime)s %(levelname)s %(module)s',
        },
        'simple': {
            'format': '%(asctime)s %(levelname)s %(message)s',
        },
        'formatter_console_warning': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s',
        },
        'formatter_errors': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s %(exc_info)s',
        },
        'formatter_security': {
            'format': '%(asctime)s %(levelname)s %(module)s %(message)s',
        },
        'formatter_mail': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s ',
        },

    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        # 'filter_debug_level': {
        #     '()': 'logging_formatter.log_middleware.FilterLevels',
        #     'filter_levels': [
        #         "DEBUG"
        #     ]
        # },
        # 'filter_info_level': {
        #     '()': 'logging_formatter.log_middleware.FilterLevels',
        #     'filter_levels': [
        #         "INFO"
        #     ]
        # },
        #
        # 'filter_warning_level': {
        #     '()': 'logging_formatter.log_middleware.FilterLevels',
        #     'filter_levels': [
        #         "WARNING"
        #     ]
        # },
        # 'filter_error_level': {
        #     '()': 'logging_formatter.log_middleware.FilterLevels',
        #     'filter_levels': [
        #         "ERROR"
        #     ]
        # },
        # 'filter_critical_level': {
        #     '()': 'logging_formatter.log_middleware.FilterLevels',
        #     'filter_levels': [
        #         "CRITICAL"
        #     ]
        # },

    },
    'handlers': {
        'console_error': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'formatter_errors',
        },

        'console_warning': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'formatter_console_warning'
        },

        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.FileHandler',
            'filename': 'console.log',
            'formatter': 'simple'
        },

        'general': {
            'level': 'INFO',
            # 'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'filename': 'general.log',
            'formatter': 'general'
        },
        'errors': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'errors.log',
            'formatter': 'formatter_errors'

        },
        'security': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'security.log',
            'formatter': 'formatter_security'

        },
        'mail_admins': {
            'level': 'WARNING',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            # 'include_html': True,
            'formatter': 'formatter_mail'

        },
    },
    'loggers': {
        'django': {
            'level': 'DEBUG',
            'handlers': ['console', 'console_warning', 'console_error', 'general', 'errors'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console','errors', 'mail_admins'],
            'propagate': True,
        },
        'django.server': {
            'handlers': ['errors', 'mail_admins'],
            'propagate': True,
        },
        'django.template': {
            'handlers': ['errors'],
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['errors'],
            'propagate': True,
        },
        'django.security': {
            'handlers': ['security'],
            'propagate': True,
        },

    }
}
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],}
CORS_ALLOW_ALL_ORIGINS = True
