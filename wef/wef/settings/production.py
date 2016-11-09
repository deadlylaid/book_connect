from .partials import *

DEBUG = False

ALLOWED_HOSTS = ['*']

STATICFILES_STORAGE = 'wef.storage.S3PipelineManifestStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_ACCESS_KEY_ID = 'AKIAIANK2NNJ47OHD5YA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'nsuconnect'
