import logging.config

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(levelname)s - %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'simple',
            'stream': 'ext://sys.stdout'
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'simple',
            'filename': 'app_monitoring.log', 
            'maxBytes': 300000000, # 300Mb
            'backupCount': 3
        }
    },
    'loggers': {
        'monitoring': {
            'level': 'DEBUG',
            'handlers': ['file'],
            'propagate': False
        }
    }
})

if __name__ == "__main__":
    logger = logging.getLogger('monitoring')
    logger.debug('This is a debug message')
