from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('regular', 'Обычный работник'),
        ('admin', 'Администратор'),
    )

    user_type = models.CharField(
        max_length=10,
        choices=USER_TYPE_CHOICES,
        default='regular',
        verbose_name='Тип пользователя'
    )

    @property
    def is_admin(self):
        return self.user_type == 'admin' or self.is_superuser

    @property
    def is_employee(self):
        return self.user_type == 'regular'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'