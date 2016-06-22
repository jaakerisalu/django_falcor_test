"""
Django settings for Falcor Test project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import os

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# Build paths inside the project like this: os.path.join(SITE_ROOT, ...)
SITE_ROOT = os.path.dirname(os.path.dirname(__file__))


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True

ADMINS = (
    ('Thorgate admins', 'errors@thorgate.eu'),
)
MANAGERS = ADMINS
EMAIL_SUBJECT_PREFIX = '[Falcor Test] '  # subject prefix for managers & admins

SESSION_COOKIE_NAME = 'django_falcor_test_ssid'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'crispy_forms',
    'webpack_loader',

    'accounts',
    'django_falcor_test',
]


MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


TEMPLATE_CONTEXT_PROCESSORS = [
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'django_falcor_test.context_processors.settings_export',
]
TEMPLATE_LOADERS = [
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
]
TEMPLATE_DIRS = [
    os.path.join(SITE_ROOT, 'templates'),
]


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(SITE_ROOT, 'db.sqlite3'),
    }
}


# Caching
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'KEY_PREFIX': 'django_falcor_test',
    }
}


# Internationalization
LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', 'English'),
    ('et', 'Eesti keel'),
)
LOCALE_PATHS = (
    'locale',
)

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files and media (CSS, JavaScript, images)
MEDIA_ROOT = os.path.join(SITE_ROOT, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(SITE_ROOT, 'assets')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(SITE_ROOT, 'static'),
    os.path.join(SITE_ROOT, 'app', 'build'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'dummy key'

AUTH_USER_MODEL = 'accounts.User'

ALLOWED_HOSTS = []

# Static site url, used when we need absolute url but lack request object, e.g. in email sending.
SITE_URL = 'http://127.0.0.1:8000'

# Don't allow site's content to be included in frames/iframes.
X_FRAME_OPTIONS = 'DENY'


ROOT_URLCONF = 'django_falcor_test.urls'

WSGI_APPLICATION = 'django_falcor_test.wsgi.application'


LOGIN_REDIRECT_URL = '/'
LOGIN_URL = 'login'


# Crispy-forms
CRISPY_TEMPLATE_PACK = 'bootstrap3'


# Email config
DEFAULT_FROM_EMAIL = "Falcor Test <info@TODO.com>"
SERVER_EMAIL = "Falcor Test server <server@TODO.com>"

# SMTP
EMAIL_HOST = 'smtp.sparkpostmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'info@TODO.com'
EMAIL_HOST_PASSWORD = 'TODO (test api key)'


# Base logging config. Logs INFO and higher-level messages to console. Production-specific additions are in
#  production.py.
#  Notably we modify existing Django loggers to propagate and delegate their logging to the root handler, so that we
#  only have to configure the root handler.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'default': {
            'format': '%(asctime)s [%(levelname)s] %(name)s:%(lineno)d %(funcName)s - %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        }
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'django': {'handlers': [], 'propagate': True},
        'django.request': {'handlers': [], 'propagate': True},
        'django.security': {'handlers': [], 'propagate': True},
    }
}

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# Disable a few system checks. Careful with these, only silence what your really really don't need.
# TODO: check if this is right for your project.
SILENCED_SYSTEM_CHECKS = [
    'security.W001',  # we don't use SecurityMiddleware since security is better applied in nginx config
]


# Default values for sentry
RAVEN_BACKEND_DSN = ''
RAVEN_PUBLIC_DSN = ''
RAVEN_CONFIG = {}


WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': '',
        'STATS_FILE': os.path.join(SITE_ROOT, 'app', 'webpack-stats.json'),
    }
}

# All these settings will be made available to javascript app
SETTINGS_EXPORT = [
    'DEBUG',
    'SITE_URL',
    'RAVEN_PUBLIC_DSN',
]
