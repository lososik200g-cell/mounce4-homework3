from django.contrib import admin
from django.urls import path
from posts.views import post_list_view, post_detail_view  # Импортируем функции из views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', post_list_view, name='post_list'),             # Список постов и категорий
    path('posts/<int:pk>/', post_detail_view, name='post_detail'), # Деталка одного поста
]