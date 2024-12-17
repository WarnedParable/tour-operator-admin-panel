from django.db import models

class Hotel(models.Model):
    """
    Модель отеля
    """
    name = models.CharField(
        max_length=200,
        verbose_name='Название отеля'
    )
    stars = models.IntegerField(
        choices=[(i, i) for i in range(1, 6)],
        verbose_name='Количество звезд'
    )
    address = models.TextField(
        verbose_name='Адрес отеля'
    )
    country = models.ForeignKey(
        'countries.Country',
        on_delete=models.PROTECT,
        related_name='hotels',
        verbose_name='Страна'
    )

    def __str__(self):
        return f"{self.name} ({self.stars}*)"

    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'