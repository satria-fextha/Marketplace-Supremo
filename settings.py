import os

# Establecer el modo de depuración
DEBUG = False

# Configuración de allowed hosts
ALLOWED_HOSTS = ['foodbridge.net', 'www.foodbridge.net']

# Configuración de archivos estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'Funcionalidades', 'static')]

# Configuración de archivos de medios
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'Funcionalidades', 'media')

# Configuración de la base de datos
# Configuración de la base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # o cambia a 'django.db.backends.postgresql' si estás usando PostgreSQL
        'NAME': 'wbmtrlih_marketplace_database',  # Cambia esto al nombre de tu nueva base de datos
        'USER': 'wbmtrlih_jorge',  # Corrige aquí añadiendo la coma
        'PASSWORD': 'L1maperu+1',
        'HOST': 'localhost',
        'PORT': '',
    }
}
# Sección INSTALLED_APPS
INSTALLED_APPS = [
    # ... otras aplicaciones ...
    'Funcionalidades.chat',
    'Funcionalidades.notifications',
    'Funcionalidades.orders',
    'Funcionalidades.payments',
    'Funcionalidades.Products',
    'Funcionalidades.reviews',
    'Funcionalidades.users.users',
]

# ...

