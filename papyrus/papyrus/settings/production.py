from papyrus.settings.common import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'london',
        'USER': 'london',
        'PASSWORD': 'london',
        'HOST': '127.0.0.1',
        'PORT': '5433',
    }
}