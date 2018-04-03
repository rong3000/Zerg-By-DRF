"""
Django settings for Zerg project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%5$kozgmur0^2o!9#*mg+3uxvn+1u0vg*3^70gil_f&k_(63bi'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'api',

    'rest_framework',
    'rest_framework_swagger'
)

REST_FRAMEWORK = {
    # Parser classes priority-wise for Swagger
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.JSONParser',
    ],
    'EXCEPTION_HANDLER': 'api.handle.exception_handler'
}


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'Zerg.urls'

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

WSGI_APPLICATION = 'Zerg.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'zerg',
        'USER': 'root',
        'PASSWORD': 'imyuols123',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] [%(filename)s] [line:%(lineno)d]- %(message)s'
        },
    },
    'handlers': {
        # 'file_handler': {
        #     'level': 'INFO',
        #     'class': 'logging.handlers.RotatingFileHandler',
        #     'filename': os.path.join(BASE_DIR, "logs", 'debug.log'),
        #     'maxBytes': 1024 * 1024 * 5,
        #     'backupCount': 5,
        #     'formatter': 'standard'
        # },
        'console_handler': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console_handler'],
            'level': 'DEBUG',
            'propagate': True
        },
        'django.request': {
            'handlers': ['console_handler'],
            'level': 'INFO',
            'propagate': True
        },
        # 'log_to_file': {
        #     'handlers': ['file_handler'],
        #     'level': 'INFO',
        #     'propagate': True  # 是否继承父类的log信息
        # },
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

WECHAT_APPLETS = {
    'AppID': 'wx251a06917ad81304',
    'AppSecret': 'd9f3eb480c17ac01d6634a03ae3d11f3',
    'LoginURL': 'https://api.weixin.qq.com/sns/jscode2session'
}


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}