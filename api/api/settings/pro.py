from .base import *

ALLOWED_HOSTS = ["api.ardent.tech"]

CORS_ORIGIN_WHITELIST = ("ardent.tech",)

DEBUG = False

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = from_env("ARDENT_EMAIL_HOST")
EMAIL_HOST_PASSWORD = from_env("ARDENT_EMAIL_HOST_PASSWORD")
EMAIL_HOST_USER = from_env("ARDENT_EMAIL_HOST_USER")

MEDIA_ROOT = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(BASE_DIR))), "media")

STATIC_ROOT = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(BASE_DIR))), "static")
