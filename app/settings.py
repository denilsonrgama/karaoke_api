import os
from pathlib import Path
from django.core.management.utils import get_random_secret_key
from decouple import config
from dotenv import load_dotenv

# Base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / '.env')


# SECRET_KEY seguro (use variável de ambiente)
SECRET_KEY = os.getenv('SECRET_KEY', get_random_secret_key())

# DEBUG desligado em produção - alterar para true apenas em desenvolvimento
DEBUG = config('DEBUG', default=False, cast=bool)

# Hosts permitidos
ALLOWED_HOSTS = ['*']
LOGIN_REDIRECT_URL = '/karaokedocowboy/'


# Aplicações instaladas

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'rest_framework',
    'musicas'     
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',  # <-- obrigatório
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')


ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST', default='127.0.0.1'),
        'PORT': config('DB_PORT', default='5432'),
    }
}


# -----------------------
# Senhas e validação
# -----------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -----------------------
# Internacionalização
# -----------------------
USE_L10N = True
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# -----------------------
# Static & Media

MEDIA_URL = config("MEDIA_URL", default="/media/")
MEDIA_ROOT = config("MEDIA_ROOT", default=os.path.join(BASE_DIR, "media"))

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'




# -----------------------
# Sessões
# -----------------------
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # destrói sessão ao fechar navegador
SESSION_COOKIE_AGE = 3600  # opcional: tempo máximo de sessão
SESSION_COOKIE_SECURE = True  # só em HTTPS
CSRF_COOKIE_SECURE = True     # só em HTTPS
CSRF_TRUSTED_ORIGINS = ['https://*.ngrok-free.dev']  # ajuste conforme necessário
# -----------------------
# Mensagens
# -----------------------
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}

EMAIL = 'denilson.gama.drg@gmail.com'

SITE_ID = 1
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = os.getenv('SENDGRID_API_KEY')

EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'karaokedocowboy@outlook.com'

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'karaokedocowboy'
LOGOUT_REDIRECT_URL = 'login'
DEFAULT_DOMAIN = '127.0.0.1:8000'


REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 20,
}
