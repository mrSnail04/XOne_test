import os
import dj_database_url
from .base import *

SECRET_KEY = 'django-insecure-f+^ndv5sm(#8ts7$ucy^zuij6)v450-eoa08!@7!4zha#c)fb^'
DEBUG = False
ALLOWED_HOSTS = ['ancient-oasis-20487.herokuapp.com']

DATABASE_URL = os.environ.get('DATABASE_URL')
db_from_env = dj_database_url.config(
    default=DATABASE_URL, conn_max_age=500, ssl_require=True)
DATABASES['default'].update(db_from_env)