import os
from .partials import *

DEBUG = False

ALLOWED_HOSTS = ['*']

STATICFILES_STORAGE = 'wef.storage.S3PipelineManifestStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")

AWS_S3_HOST = "s3-ap-northeast-1.amazonaws.com"

#CloudFront
AWS_S3_CUSTOM_DOMAIN = 'd1s96a26nn963w.cloudfront.net'
AWS_S3_URL_PROTOCOL = 'https'

STATIC_URL = "https://d1s96a26nn963w.cloudfront.net/"
