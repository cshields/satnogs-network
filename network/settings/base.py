from os import path, getenv
BASE_DIR = path.dirname(path.dirname(__file__))


# Apps
DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
)
THIRD_PARTY_APPS = (
    'avatar',
    'rest_framework',
    'rest_framework.authtoken',
    'crispy_forms',
    'allauth',
    'allauth.account',
)
LOCAL_APPS = (
    'network.users',
    'network.base',
    'network.api',
)
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# Middlware
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

# Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
ADMINS = (
    ('SatNOGS team', 'info@satnogs.org'),
)
MANAGERS = ADMINS

# Cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake'
    }
}

# Internationalization
TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Templates
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',

    'allauth.account.context_processors.account',

    'network.base.context_processors.analytics',
    'network.base.context_processors.stage_notice',
)
TEMPLATE_DIRS = (
    path.join(BASE_DIR, 'templates'),
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# Static & Media
STATIC_ROOT = path.join(path.dirname(BASE_DIR), 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    path.join(BASE_DIR, 'static'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
MEDIA_ROOT = path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
CRISPY_TEMPLATE_PACK = 'bootstrap3'
STATION_DEFAULT_IMAGE = '/static/img/dish.png'

# App conf
ROOT_URLCONF = 'network.urls'
WSGI_APPLICATION = 'network.wsgi.application'
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# Auth
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)
ACCOUNT_ADAPTER = 'network.users.adapter.NoSignupsAdapter'
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
AUTH_USER_MODEL = 'users.User'
LOGIN_REDIRECT_URL = 'users:redirect_user'
LOGIN_URL = 'account_login'
AUTOSLUG_SLUGIFY_FUNCTION = 'slugify.slugify'

# Logging
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

# API
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.DjangoFilterBackend',
    )
}

# Security
SECRET_KEY = getenv('SECRET_KEY', 'changeme')

# Database
import dj_database_url
DATABASE_URL = getenv('DATABASE_URL', 'sqlite:///db.sqlite3')
DATABASES = {'default': dj_database_url.parse(DATABASE_URL)}

# Mapbox API
MAPBOX_GEOCODE_URL = 'https://api.tiles.mapbox.com/v4/geocode/mapbox.places/'
MAPBOX_MAP_ID = getenv('MAPBOX_MAP_ID', '')
MAPBOX_TOKEN = getenv('MAPBOX_TOKEN', '')

# Observations datetimes in minutes
DATE_MIN_START = '60'
DATE_MAX_RANGE = '480'

# Station heartbeat in minutes
STATION_HEARTBEAT_TIME = 60

# DB API
DB_API_ENDPOINT = getenv('DB_API_ENDPOINT', 'https://db.satnogs.org/api/')
