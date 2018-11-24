import os

import dj_database_url

from .settings import *


DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'))
    }

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS'), 'localhost']
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
SECRET_KEY = os.environ.get('SECRET_KEY')
