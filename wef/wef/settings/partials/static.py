import os
from .base import BASE_DIR


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'wef', 'static')
        ]

AUTH_USER_MODEL = 'users.User'
