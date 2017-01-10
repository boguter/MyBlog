# coding=utf-8
"""
Django settings for MyBlog project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from django.conf.locale.en import formats as formats_en

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5@mw^m6i-hz=yo3u&4+65r$&!ke^2upp@tvu&t*q^_mfc1pbm-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["blog.tangyingkang.com", "localhost"]

#
DUOSHUO_SECRET = "74cd6131489314687b1433fceb9aa985"
DUOSHUO_SHORT_NAME = "eacon"

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'blog',

    'duoshuo',

)

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

ROOT_URLCONF = 'MyBlog.urls'

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
                # add for django-pagination
                "django.core.context_processors.i18n",
                "django.core.context_processors.media",
            ],
        },
    },
]

WSGI_APPLICATION = 'MyBlog.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'USER': str(os.environ.get('MYSQL_USER')),
        'PASSWORD': str(os.environ.get('MYSQL_PASSWORD')),
        'HOST': '127.0.0.1',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

# use qiniu CDN
# STATIC_URL = 'http://7xsqab.com1.z0.glb.clouddn.com/'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_BLOG = os.path.join(BASE_DIR, 'blog', 'static')
STATICFILES_DIRS = (
    STATIC_BLOG,
)
STATIC_ARTICLE_PATH = os.path.join(STATIC_URL, 'html')

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates"),
)

# display formated datetime field on django-admin
formats_en.DATETIME_FORMAT = 'Y-m-d H:m:s'

# URL prefix for internet access
# ex: if the website is served on 'http://www.example.com/blog/', then '/blog' is the prefix
URL_PREFIX = ""

# show "techblog" at navbar or not
# TECHBLOG_AT_NAVBAR = True

# django-rest-fromework
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

# mdfiles export dir
MDFILES_DIR = os.path.join(BASE_DIR, 'mdfile')

# blog page served as static html file
STATIC_PAGE = True
STATIC_PAGE_DIR = os.path.join(BASE_DIR, 'static_page')

# redirect to this url after login success
LOGIN_REDIRECT_URL = '/'

# cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'blog_cache',
    }
}

# pagination
BLOG_EACH_PAGE = 10
WEIBO_EACH_PAGE = 5

#
MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')
MEDIA_URL = '/static/media/'
