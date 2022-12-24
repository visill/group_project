import environ

from pathlib import Path
from sorl.thumbnail import delete
from django_cleanup.signals import cleanup_pre_delete

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    DEBUG=(bool, True),
    SECRET_KEY=(str, "django-insecure-had=notsecretkey"),
    EMAIL=(str, "example@example.com"),
)

environ.Env.read_env(BASE_DIR / ".env", overwrite=True)

SECRET_KEY = env("SECRET_KEY")

DEBUG = env("DEBUG")

ALLOWED_HOSTS = ["*"]

INTERNAL_IPS = [
    "127.0.0.1",
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "sorl.thumbnail",
    "django_cleanup.apps.CleanupConfig",

    "museums.apps.MuseumsConfig",
    "homepage.apps.HomepageConfig",
    "exhibits.apps.ExhibitsConfig",
    "events.apps.EventsConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "group_project.urls"

TEMPLATE_DIRS = [
    BASE_DIR / "templates"
]
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": TEMPLATE_DIRS,
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "group_project.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "NumericPasswordValidator"
        ),
    },
]

LANGUAGE_CODE = "ru-RU"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_ROOT = BASE_DIR / "static"
STATIC_URL = "/static/"

STATICFILES_DIRS = [BASE_DIR / "static_dev"]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"


def sorl_delete(**kwargs):
    delete(kwargs["file"])


cleanup_pre_delete.connect(sorl_delete)
