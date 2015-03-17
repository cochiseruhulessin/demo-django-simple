

DEBUG = True


# A 128-character string with a high entropy.
SECRET_KEY = (
    'ec4d091dff784516a862ef0169a34136'
    '4eb5087a4afd4783ae4a1d8aa81b29c5'
    '4d8f27b31e1f47d898ff0937db4d44bd'
    'fe83b22cdd1f466fa469c0c77a7e2b2c'
)


#: Specifies the installed Django applications
INSTALLED_APPS = (
    'django.contrib.sessions',
    'django.contrib.messages',
    'django_jinja',
)


# The URL configuration used by Django to dispatch requests to the
# appropratie request handlers.
ROOT_URLCONF = 'demo.urls'


# The Data Source Name (DSN) of the database.
DATABASE_DSN = 'sqlite:///database.db'


# Loader classes used to find templates.
TEMPLATE_LOADERS = (
    'django_jinja.loaders.FileSystemLoader',
    'django_jinja.loaders.AppLoader',
)


# Extension for Jinja templates
DEFAULT_JINJA2_TEMPLATE_EXTENSION = '.j2'


# A list of directories where templates can be found
TEMPLATE_DIRS = [
    'share/templates',
    '../share/templates'
]


# Request middleware
MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]


TEMPLATE_CONTEXT_PROCESSORS = [
    'django.contrib.messages.context_processors.messages'
]


# Specifies the storage backend for messages
SESSION_ENGINE = 'django.contrib.sessions.backends.file'
