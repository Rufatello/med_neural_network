from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Specification(models.Model):
    name = models.CharField(verbose_name='Название', max_length=150)
    descriptions = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Спецификация'
        verbose_name_plural = 'Спецификации'


class User(AbstractUser):
    state_user = [
        ('doctor', 'Врач'),
        ('patient', 'Пациент'),
    ]

    username = None
    email = models.EmailField(unique=True, max_length=70, verbose_name='Почта')
    first_name = models.CharField(verbose_name='Имя', max_length=70)
    last_name = models.CharField(verbose_name='Фамилия', max_length=70)
    surname = models.CharField(verbose_name='Отчество', max_length=70, **NULLABLE)
    state = models.CharField(default='patient', choices=state_user, verbose_name='Статус')
    code = models.CharField(max_length=15, verbose_name='код', **NULLABLE)
    phone = models.CharField(max_length=20, **NULLABLE, verbose_name='Телефон')
    avatar = models.ImageField(upload_to='users', **NULLABLE)
    specification = models.ForeignKey(Specification, on_delete=models.CASCADE, **NULLABLE)
    is_active = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
