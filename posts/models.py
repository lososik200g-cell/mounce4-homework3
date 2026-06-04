from django.db import models

# Модель Категории (уже должна быть у вас)
class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название категории")
    description = models.TextField(verbose_name="Описание категории")
    is_active = models.BooleanField(default=True, verbose_name="Активна")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


# НОВАЯ модель Тега (Многие ко многим)
class Tag(models.Model):
    title = models.CharField(max_length=255, verbose_name="Тег")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


# Обновленная модель Поста
class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='posts/', blank=True, null=True, verbose_name="Картинка")
    
    # СВЯЗИ из 3-го урока:
    #ForeignKey (Один ко многим): если удалить категорию, пост останется (SET_NULL)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Категория")
    # ManyToManyField (Многие ко многим): у поста может быть много тегов
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="Теги")

    # ДАТЫ из 3-го урока:
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания") # Ставится при создании
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")   # Меняется при каждом сохранении

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"