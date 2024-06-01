"""
ASGI config for webchatapp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import protocolTypeRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webchatapp.settings')

application = protocolTypeRouter({
    'http':get_asgi_application()
})
