import os
from eqar_backend.settings import BASE_DIR

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [ 'localhost' ]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/api/static/'
#STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), '/files/static/')

MEDIA_URL = '/reports/'
MEDIA_ROOT = '/api/reports/'
#MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), '/files/reports/')

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'mail.example.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'noreply@example.com'
EMAIL_HOST_PASSWORD = 'topsecret'
EMAIL_FROM = 'backend-test@example.com'
EMAIL_CC = [ 'admin@example.com' ]
EMAIL_TO = [ 'to@example.com' ]

ADMINS = [ ('Admin', 'admin@example.com')]
SERVER_EMAIL = 'backend-test@example.com'

# CELERY STUFF
CELERY_BROKER_URL = 'redis://redis:6379'
CELERY_RESULT_BACKEND = 'redis://redis:6379'
CELERY_ACCEPT_CONTENT = [ 'application/json' ]
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Europe/Brussels'

SUIT_CONFIG = {
    'ADMIN_NAME': 'DEQAR Administration (DEV)',
    'LIST_PER_PAGE': 15,
    'SEARCH_URL': '/admin/auth/user/',
    'MENU_ICONS': {
       'sites': 'icon-leaf',
       'auth': 'icon-lock',
    },
}

DEFAULT_FROM_EMAIL = 'backend-test@example.com'

DOMAIN = 'localhost'
SITE_NAME = 'DEQAR-DEV'

DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': 'https://admin.example.com/password-reset/{uid}/{token}',
    'PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND': True,
    'ACTIVATION_URL': '#/activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': False,
    'SERIALIZERS': {
        'current_user': 'accounts.serializers.CurrentUserSerializer',
    },
}

SWAGGER_SETTINGS = {
   'SECURITY_DEFINITIONS': {
      'Bearer': {
            'type': 'apiKey',
            'name': 'Bearer',
            'in': 'header'
      }
   }
}

# SOLR SETTINGS
SOLR_URL = "http://solr:8983/solr"
SOLR_CORE_INSTITUTIONS = 'deqar-institutions'
SOLR_CORE_AGENCIES = 'deqar-agencies'
SOLR_CORE_REPORTS = 'deqar-reports'
SOLR_CORE_REPORTS_V3 = 'deqar-reports-v3'

# Meilisearch
MEILI_API_URL = "http://meili:7700"
#MEILI_API_KEY

# settings for VC issuance
LETSTRUST_EQAR_EBSI_DID = "did:ebsi:..."
LETSTRUST_EQAR_DID = "did:web:..."
LETSTRUST_CORE_API = 'http://ssikit:7000/v1'
LETSTRUST_SIGNATORY_API = 'http://ssikit:7001/v1'

DEQAR_REPORT_URI = 'https://.../%s'
DEQAR_AGENCY_URI = 'https://.../%s'
DEQAR_INSTITUTION_URI = 'https://.../%s'
DEQAR_COUNTRY_URI = 'https://.../%s'

VC_CACHE_MAX_AGE = 300

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# OrgReg sync
ORGREG_API_RETRY = 3
ORGREG_API_KEY = '...'

