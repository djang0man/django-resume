import os

from .settings import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'resume',
        'USER': 'stuartdkershaw',
        'PASSWORD': 'honeywellZima800',
        'HOST': 'django.ceynhz03xnah.us-west-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}
DEBUG = False
TEMPLATE_DEBUG = False
SECURE_SSL_HOST = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS'), 'localhost']
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
SECRET_KEY = os.environ.get('SECRET_KEY')
