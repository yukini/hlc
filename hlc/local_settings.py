import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@2m=vjonnsl7h_88p%_8zfx_(@qgnx2t-70s+7k@z9oe3avw2q'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ain',
        'USER': 'yukini',
        'PASSWORD': 'testuser',
        'HOST': '192.168.33.10',
        'PORT': 5432,
    }
}

DEBUG = True

# override
STATIC_PRECOMPILER_DISABLE_AUTO_COMPILE = False

print(SECRET_KEY)