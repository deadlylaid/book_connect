import os
from .base import BASE_DIR, PROJECT_BASE_DIR


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(PROJECT_BASE_DIR, "dist", "static")


# PIPELINE #

# Location of collect staticfiles
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

# config where is staticfiles
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

PIPELINE = {
    'STYLESHEETS': {
        'bookconnect': {
            'source_filenames': (
                'css/application.css',
            ),
            'output_filename': 'css/bookconnect.css',
        },
    },
    'JAVASCRIPT': {
        'csrftoken': {
            'source_filenames': (
                'js/csrf_token.js',
            ),
            'output_filename': 'js/csrf_token.js',
        },
        'items': {
            'source_filenames': (
                'js/booksale.js',
                'js/detail.js',
            ),
            'output_filename': 'js/items.js',
        },
        'users': {
            'source_filenames': (
                'js/users/aftersocial.js',
                'js/users/joinus.js',
            ),
            'output_filename': 'js/users/users.js',
        },
    }
}


PIPELINE['CSS_COMPRESSOR'] = 'pipeline.compressors.yuglify.YuglifyCompressor'
