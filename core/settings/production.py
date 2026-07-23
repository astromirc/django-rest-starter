from .base import *

DEBUG = False

# Hosts
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
CSRF_TRUSTED_ORIGINS = ALLOWED_HOSTS

# Cors
CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS")

# Production applications
INSTALLED_APPS += ["storages"]

# Middlewares
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

# Storage backends
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Static files
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# Media files
MEDIA_URL = "/media/"

# Security
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_SECONDS = 300

# AWS S3
AWS_STORAGE_BUCKET_NAME = env.str("AWS_S3_BUCKET_NAME")
AWS_QUERYSTRING_EXPIRE = 300
AWS_DEFAULT_ACL = "private"
AWS_QUERYSTRING_AUTH = True
