from base import *

ENVIRONMENT = 'dev'

# Debug
DEBUG = True
MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

# override for INTERNAL_IPS, for docker and envs where that is dynamic
def show_toolbar(request):
    return True

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
    'SHOW_TOOLBAR_CALLBACK': show_toolbar
}

# Apps
INSTALLED_APPS += ('debug_toolbar',)

# Mail
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
