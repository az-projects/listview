# -*- coding: utf-8 -*-
import os
# Django settings for listview project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = ( 
    ( 'tony', 'Tangxuguo@gmail.com' ),
    ( 'willard', 'yongyuanstu@gmail.com' ),
 )

MANAGERS = ADMINS

if 'SERVER_SOFTWARE' in os.environ:
    # SAE 用，根据 SAE  MYSQL数据库配置填写下面参数，一般都是这样的
    import sae.const 
    MYSQL_DB = sae.const.MYSQL_DB 
    MYSQL_USER = sae.const.MYSQL_USER 
    MYSQL_PASS = sae.const.MYSQL_PASS 
    MYSQL_HOST_M = sae.const.MYSQL_HOST 
    MYSQL_HOST_S = sae.const.MYSQL_HOST_S 
    MYSQL_PORT = sae.const.MYSQL_PORT
else:
    # Local 本地调试用，便于导出数据库,根据本地MYSQL数据库填写下面参数
    MYSQL_DB = 'test' 
    MYSQL_USER = 'root' 
    MYSQL_PASS = '' 
    MYSQL_HOST_M = '127.0.0.1' 
    MYSQL_HOST_S = '127.0.0.1' 
    MYSQL_PORT = '3306' 

DATABASES = { 
    'default': { 
        'ENGINE': 'django.db.backends.mysql',
        'NAME': MYSQL_DB,
        'USER': MYSQL_USER,
        'PASSWORD': MYSQL_PASS,
        'HOST': MYSQL_HOST_M,
        'PORT': MYSQL_PORT,
    } 
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.4/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'zh-cn'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = ( 
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
 )

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = ( 
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
 )

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'tj(i7q&amp;s%dm)@s_bh!l!6$^_fxf!2f6kod6j&amp;8apnc+x34vv81'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = ( 
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
 )

MIDDLEWARE_CLASSES = ( 
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
 )

ROOT_URLCONF = 'listview.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'listview.wsgi.application'

TEMPLATE_DIRS = ( 
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
 )
TEMPLATE_DIRS += ( os.path.join( os.path.dirname( "__file__" ), 'templates' ) , )

STATICFILES_DIRS += ( os.path.join( os.path.dirname( "__file__" ), 'static' ) , )

INSTALLED_APPS = ( 
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
     'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'readlist',
    'django-groundwork',
 )

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
