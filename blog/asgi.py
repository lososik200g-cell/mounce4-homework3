import os

from django.core.asgi import get_asgi_application

# Исправленный путь: blog.blog.settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.blog.settings')

application = get_asgi_application()