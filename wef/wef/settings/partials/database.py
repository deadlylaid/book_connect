import os

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bookconnect',
        'USER': 'hanminsoo',
        'PASSWORD': 'deadlylaid',
        'HOST': '',
    }
}
