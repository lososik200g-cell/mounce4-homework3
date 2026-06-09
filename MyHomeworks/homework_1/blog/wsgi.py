import os

from django.core.wsgi import get_wsgi_application

# Исправленный путь: blog.blog.settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.blog.settings')

application = get_wsgi_application()