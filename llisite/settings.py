"""
Django settings for llisite project.

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

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = os.getenv('DJANGO_DEBUG') != 'FALSE'
# SECURITY WARNING: keep the secret key used in production secret!
if DEBUG:
    SECRET_KEY = 't$z*-(o-c3%x+o%*z)duu9%0_^sr_w$$lfa%(^iipb5!wp!ftc'
else:
    SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!

if DEBUG:
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = ['lightandleadership.pythonanywhere.com', 'lightandleadership.com']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'content',
    'spanish_content',
    'tinymce',
)
SITE_ID = 3
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware' ,
)

ROOT_URLCONF = 'llisite.urls'

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
                'content.context_processors.footer',
                'content.context_processors.navbar',
                'spanish_content.context_processors.spanish_navbar',
            ],
        },
    },
]

WSGI_APPLICATION = 'llisite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# TINYMCE_JS_URL = 'http://debug.example.org/tiny_mce/tiny_mce_src.js'
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,xhtmlxtras,spellchecker,paste,searchreplace, save, advhr, advimage, advlink, emotions, iespell, insertdatetime, preview, media",
    'theme_advanced_buttons1': "bold,italic,underline,strikethrough,sub,sup,separator,justifyleft,justifycenter,justifyright,justifyfull,separator,formatselect,fontselect,fontsizeselect",
    'theme_advanced_buttons2': "bullist,numlist,outdent,indent,ltr,rtl,separator,link,unlink,anchor,image,separator,table,insertdate,inserttime,advhr,emotions,media,charmap,separator,undo,redo",
    'theme': 'advanced',
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
    'elementpath': False,
    'height': 300,
    'width': 1000,
    'resize': 'both',
    "extended_valid_elements" : "iframe[src|frameborder|style|scrolling|class|width|height|name|align]",

}
TINYMCE_SPELLCHECKER = True
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
