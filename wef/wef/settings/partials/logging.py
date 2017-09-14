from .base import BASE_DIR

import os


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
