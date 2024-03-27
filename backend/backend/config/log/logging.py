import os

current_dir = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))


SET_LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "file_format": {
            "format": "[%(asctime)s] %(levelname)s|%(module)s: %(message)s",
            "datefmt": "%d.%m.%Y %H:%M:%S",
        },
        "error_format": {
            "format": "[%(asctime)s - %(levelname)s] %(message)s, PATH: %(pathname)s, line: %(lineno)d",
            "datefmt": "%d.%m.%Y %H:%M:%S",
        },
        "security_error": {
            "format": "[%(asctime)s] - [%(levelname)s] - [%(module)s] - %(message)s",
            "datefmt": "%d/%m/%Y %H:%M:%S",
        },
        "verbose": {
            "format": "[%(asctime)s] - [%(levelname)s] - [%(module)s] - %(message)s",
            "datefmt": "%d/%m/%Y %H:%M:%S",
        },
    },
    "handlers": {
        "errors": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(BASE_DIR, "logs/errors.log"),
            "maxBytes": 1024 * 1024 * 5,
            "backupCount": 5,
            "formatter": "error_format",
            "level": "ERROR",
        },
        "security": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(BASE_DIR, "logs/security.log"),
            "maxBytes": 1024 * 1024 * 5,
            "backupCount": 5,
            "formatter": "security_error",
            "level": "INFO",
        },
        "telegram_bot": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(BASE_DIR, "logs/telegram_bot.log"),
            "maxBytes": 1024 * 1024 * 5,
            "backupCount": 5,
            "formatter": "error_format",
            "level": "ERROR",
        },
        "payment_create": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(BASE_DIR, "logs/payment_create.log"),
            "maxBytes": 1024 * 1024 * 5,
            "backupCount": 5,
            "formatter": "error_format",
            "level": "ERROR",
        },
        "AdminPanel": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(BASE_DIR, "logs/Admin/AdminPanel.log"),
            "maxBytes": 1024 * 1024 * 5,
            "backupCount": 5,
            "formatter": "error_format",
            "level": "ERROR",
        },
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django.request": {"handlers": ["errors"], "level": "ERROR", "propagate": True},
        "django.security": {
            "handlers": ["security"],
            "level": "INFO",
            "propagate": True,
        },
        "tg_bot": {
            "handlers": ["telegram_bot"],
            "level": "ERROR",
            "propagate": True,
        },
        "payment_create": {
            "handlers": ["payment_create"],
            "level": "ERROR",
            "propagate": True,
        },
        "AdminPanel": {
            "handlers": ["AdminPanel"],
            "level": "ERROR",
            "propagate": True,
        },
        "debug": {
            "handlers": ["console"],
            "level": "INFO",
        },
    },
}
