import os

from .base import BASE_DIR

# Python Social auth

AUTHENTICATION_BACKENDS = (
        # Facebook Social auth
        'social.backends.facebook.FacebookOAuth2',
        # Kakao talk Social auth
        'social.backends.kakao.KakaoOAuth2',
        # django defualt
        'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_URL_NAMESPACE = 'social'

# Facebook App key
SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get("FACEBOOK_KEY")
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get("FACEBOOK_SECRET")
SOCIAL_AUTH_FACEBOOK_APP_NAMESPACE = os.environ.get("FACEBOOK_APP_NAMESPACE")

# Kakao App key
SOCIAL_AUTH_KAKAO_KEY = os.environ.get("KAKAO_KEY")
SOCIAL_AUTH_KAKAO_SECRET = os.environ.get("KAKAO_SECRET")

# Config redirect URL after Social sign up
LOGIN_REDIRECT_URL = '/aftersocial/'

# Config redirect when user Authentication process canceled
SOCIAL_AUTH_LOGIN_ERROR_URL = '/'

# Social Auth login process customizing
SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',

    'wef.utils.utils.get_username',

    'social.pipeline.social_auth.associate_by_email',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
)
