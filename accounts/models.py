from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    GENDER_CHOICES = [
        ('man', "Мужчина"),
        ('woman', "Женщина")
    ]
    avatar = models.ImageField(upload_to='users/avatars/', verbose_name='Аватар')
    user_information = models.TextField(null=True, blank=True, verbose_name='Информация о пользователе')
    phone_number = models.CharField(max_length=16, null=True, blank=True, verbose_name='номер телефона')
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True, blank=True, verbose_name='пол')
