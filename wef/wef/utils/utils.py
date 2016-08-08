from social.pipeline.user import get_username as social_get_username
from random import randrange


def get_username(strategy, details, user=None, *args, **kwargs):
    result = social_get_username(strategy, details, user=user, *args, **kwargs)
    result['username'] = '-'.join([
        result['username'], str(randrange(0, 9000))
    ])
    return result
