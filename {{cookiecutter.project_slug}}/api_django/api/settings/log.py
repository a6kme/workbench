import json
import logging
import os


class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            'levelname': record.levelname,
            'asctime': self.formatTime(record, self.datefmt),
            'pathname': record.pathname,
            'module': record.module,
            'lineno': record.lineno,
            'message': record.getMessage(),
        }
        return json.dumps(log_record)


def get_logging_config(base_dir, debug):
    return {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'json': {
                '()': JSONFormatter
            },
            'verbose': {
                'format': '{levelname} {asctime} {module} {message}',
                'style': '{',
            },
            'simple': {
                'format': '{levelname} {message}',
                'style': '{',
            },
        },
        'handlers': {
            'console': {
                'level': 'DEBUG' if debug else 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'simple',
            },
            'file': {
                'level': 'DEBUG' if debug else 'INFO',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(base_dir, 'django.log'),
                'maxBytes': 1024 * 1024 * 5,  # 5MB
                'backupCount': 5,  # Keep 5 backup files
                'formatter': 'json',
            },
        },
        'loggers': {
            'django': {
                'handlers': ['console'],
                'level': 'DEBUG' if debug else 'INFO',
                'propagate': True,
            },
        }
    }
