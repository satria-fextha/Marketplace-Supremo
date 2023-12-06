# Configuración de la base de datos
# las_10_funcionalidades/settings.py

import os

# Establecer el modo de depuración
DEBUG = False

# Configuración de allowed hosts
ALLOWED_HOSTS = ['foodbridge.net', 'www.foodbridge.net']

# Configuración de archivos estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'LAS 10 FUNCIONALIDADES', 'static')]

# Configuración de archivos de medios
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'LAS 10 FUNCIONALIDADES', 'media')

# Configuración de la base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # o cambia a 'django.db.backends.postgresql' si estás usando PostgreSQL
        'NAME': 'wbmtrlih_miapp',  # El nombre de tu base de datos
        'USER': 'wbmtrlih_jorge',  # Tu nombre de usuario
        'PASSWORD': 'L1maperu+1',  # La contraseña que estableciste
        'HOST': 'localhost',  # Como te indicaron, será 'localhost'
        'PORT': '',  # Deja en blanco para el puerto por defecto
    }
}

# Sección INSTALLED_APPS
INSTALLED_APPS = [
    # ... otras aplicaciones ...INSTALLED_APPS = [
    'channels',
    'Products',
    'chat',
    'notifications',
    'orders',
    'payments',
    'reviews',
    'users.users',

MIDDLEWARE = [
    ...
    'channels.middleware.ChannelMiddleware',]