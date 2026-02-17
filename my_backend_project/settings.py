from pathlib import Path
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-0p1_j_k%k@joomj=(g&@8bwv5i4n=m_gb53u_a(*%)q6k&nt2y'

# ======================
# DEBUG & Hosts
# ======================
DEBUG = True          # 🔹 actif pour dev / test
ALLOWED_HOSTS = ["*"]  # 🔹 autorise toutes les adresses

# ======================
# Applications
# ======================
INSTALLED_APPS = [
    'api',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
]

AUTH_USER_MODEL = 'api.User'

# ======================
# Middleware
# ======================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',   # ✅ static prod
    'corsheaders.middleware.CorsMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ======================
# CORS - autoriser tout
# ======================
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

# ======================
# Templates
# ======================
ROOT_URLCONF = 'my_backend_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'my_backend_project.wsgi.application'

# ======================
# Database
# ======================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ======================
# Password validation
# ======================
AUTH_PASSWORD_VALIDATORS = []

# ======================
# Internationalization
# ======================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Abidjan'
USE_I18N = True
USE_TZ = True

# ======================
# Static files
# ======================
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ======================
# Django REST Framework
# ======================
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.AllowAny",  # 🔹 autorise tout le monde
    ),
}

# ======================
# JWT
# ======================
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "AUTH_HEADER_TYPES": ("Bearer",),
}

# ======================
# Default PK
# ======================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
