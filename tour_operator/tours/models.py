from django.db import models

class Tour(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Название тура'
    )
    duration = models.IntegerField(
        verbose_name='Длительность тура (дней)'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена тура'
    )
    country = models.ForeignKey(
        'countries.Country',
        on_delete=models.PROTECT,
        related_name='tours',
        verbose_name='Страна тура'
    )
    hotel = models.ForeignKey(
        'hotels.Hotel',
        on_delete=models.PROTECT,
        related_name='tours',
        verbose_name='Отель тура'
    )

    def __str__(self):
        return f"{self.name} - {self.duration} дней"

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'