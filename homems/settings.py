import os
import pymysql

pymysql.install_as_MySQLdb()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = 'edk-i7b!m^c@((zdi=lzdm^6bd9z0mec3-$%7m9(p)i9)+v2d6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
<<<<<<< HEAD
    'mainapp'
=======
    'userapp',
    'orderapp',
    'msgapp',
    'mainapp',
    'tinymce'
>>>>>>> 878b70e9a2d0381ca4f8ea0dfc7c016c12bdd579
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'middleware.LoginMiddleware',
    'django.middleware.common.CommonMiddleware',
<<<<<<< HEAD
    'django.middleware.csrf.CsrfViewMiddleware',
=======
>>>>>>> 878b70e9a2d0381ca4f8ea0dfc7c016c12bdd579
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'homems.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'homems.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
<<<<<<< HEAD
=======
        # 'HOST': '114.116.245.220',
>>>>>>> 878b70e9a2d0381ca4f8ea0dfc7c016c12bdd579
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': 'root',
        # 'PASSWORD': '123456',
        'PASSWORD': '211488',
        'CHARSET': 'utf8',
        'NAME': 'pandas'
    }
}


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/s/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

MEDIA_URL = '/m/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

<<<<<<< HEAD


=======
TINYMCE_DEFAULT_CONFIG = {
    'theme': 'advanced',
    'width': 800,
    'height': 600
}
>>>>>>> 878b70e9a2d0381ca4f8ea0dfc7c016c12bdd579
