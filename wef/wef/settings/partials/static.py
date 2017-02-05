import os
from .base import BASE_DIR, PROJECT_BASE_DIR


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_BASE_DIR, "dist", "static")
MEDIA_ROOT = os.path.join(PROJECT_BASE_DIR, "dist", "media")

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
        'booksale': {
            'source_filenames': (
                'js/booksale.js',
            ),
            'output_filename': 'js/booksale.js',
        },
        'detail': {
            'source_filenames': (
                'js/detail.js',
            ),
            'output_filename': 'js/detail.js',
        },
        'list': {
            'source_filenames': (
                'js/list.js',
            ),
            'output_filename': 'js/list.js',
        },
        'aftersocial': {
            'source_filenames': (
                'js/users/aftersocial.js',
            ),
            'output_filename': 'js/users/aftersocial.js',
        },
        'joinus': {
            'source_filenames': (
                'js/users/joinus.js',
            ),
            'output_filename': 'js/users/joinus.js',
        },
    }
}


PIPELINE['CSS_COMPRESSOR'] = 'pipeline.compressors.yuglify.YuglifyCompressor'
PIPELINE['JS_COMPRESSOR'] = 'pipeline.compressors.yuglify.YuglifyCompressor'
