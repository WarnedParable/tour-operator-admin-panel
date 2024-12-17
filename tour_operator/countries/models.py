from django.db import models

class Country(models.Model):
    code = models.CharField(
        max_length=10,
        unique=True,
        verbose_name='Код страны'
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Название страны'
    )

    def __str__(self):
        return f"{self.name} ({self.code})"

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'