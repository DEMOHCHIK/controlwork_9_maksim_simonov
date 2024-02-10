from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')

    def __str__(self):
        return self.name


class Advertisement(models.Model):
    STATUS_CHOICES = (
        ('Pending moderation', 'На модерацию'),
        ('Published', 'Опубликовано'),
        ('Rejected', 'Отклонено'),
        ('Pending deletion', 'На удаление'),
    )
    photo = models.ImageField(upload_to='publications/photos/', blank=True, null=True, verbose_name='Фото')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE, verbose_name='Автор')
    category = models.ForeignKey('webapp.Category', on_delete=models.CASCADE, verbose_name='Категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending moderation', verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    published_at = models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField(verbose_name='Комментарий')
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE, verbose_name='Автор')
    advertisement = models.ForeignKey('webapp.Advertisement', on_delete=models.CASCADE, verbose_name='Объявление')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"Comment by {self.author.username} on {self.advertisement.title}"
