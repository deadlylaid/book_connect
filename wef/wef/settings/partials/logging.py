from .base import BASE_DIR, PROJECT_BASE_DIR

import os
import raven


SMS_LOG_FILE = os.path.abspath(os.path.join(BASE_DIR, '../sms.log'))

LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': SMS_LOG_FILE,
            },
        },
        'loggers': {
            'wef.decorators': {
                'handlers': ['file'],
                'level': 'DEBUG',
                'propagate': True,
                },
            },
    }

RAVEN_CONFIG = {
        'dsn': 'https://563061d4159f488b9e8c4f5341221540:34b0be4314dc41dab8544ab1590736c7@sentry.io/125906',
        'release': raven.fetch_git_sha(PROJECT_BASE_DIR),
        }
