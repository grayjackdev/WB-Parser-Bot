import logging
import httpx
from os import environ


class TelegramHandler(logging.Handler):
    def __init__(self, bot_token, users_id):
        super().__init__()
        self.url = f'https://api.telegram.org/bot{bot_token}' + '/sendMessage?chat_id={}&text={}'
        self.users_id = users_id

    def emit(self, record: logging.LogRecord) -> None:
        message = self.format(record)
        for user in self.users_id:
            httpx.get(self.url.format(user, message))


logger_settings = {
    'version': 1,
    'formatters': {
        'default_formatter': {
            'style': '{',
            'format': '[{levelname}] {asctime} - {module}:{lineno} >> {message}',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'default_formatter'
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/logs.log',
            'level': 'DEBUG',
            'maxBytes': 10_000_000,
            'backupCount': 3,
            'formatter': 'default_formatter'
        },
        'telegram': {
            '()': TelegramHandler,
            'level': 'ERROR',
            'formatter': 'default_formatter',
            'bot_token': environ.get('BOT_TOKEN'),
            'users_id': environ.get('ADMINS').split(',')
        }
    },
    'loggers': {
        'my_logger': {
            'level': 'DEBUG',
            'handlers': ['console', 'file', 'telegram'],
            'propagate': False
        }
    }
}
