from django.contrib import admin
from .models import Post, Category, Tag  # Импортируем еще и Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Выводим новые существующие поля: Заголовок, Дату создания и Категорию
    list_display = ('title', 'created_at', 'category')
    search_fields = ('title',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_active')
    list_filter = ('is_active',)

# Регистрируем новую модель Тегов
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')