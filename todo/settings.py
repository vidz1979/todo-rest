from decouple import config
from dj_database_url import parse as db_url
from unipath import Path

BASE_DIR = Path(__file__).parent
SECRET_KEY = config('SECRET_KEY') 
DEBUG = config('DEBUG', default=False, cast=bool)
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['.localhost', '127.0.0.1', '.herokuapp.com']

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'rest_framework',
    'corsheaders',
    'core',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
)

ROOT_URLCONF = 'todo.urls'
WSGI_APPLICATION = 'todo.wsgi.application'

DATABASES = {
    'default': config(
        'DATABASE_URL',
        default = 'sqlite:///' + BASE_DIR.child('db.sqlite3'),
        cast=db_url),
}

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Cuiaba'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
APPEND_SLASH = False

CORS_ORIGIN_ALLOW_ALL = True