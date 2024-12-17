from django.db import models

class Contract(models.Model):
    tour = models.ForeignKey(
        'tours.Tour',
        on_delete=models.PROTECT,
        related_name='contracts',
        verbose_name='Тур'
    )
    client = models.ForeignKey(
        'clients.Client',
        on_delete=models.PROTECT,
        related_name='contracts',
        verbose_name='Клиент'
    )
    contract_date = models.DateField(
        auto_now_add=True,
        verbose_name='Дата заключения договора'
    )

    def __str__(self):
        return f"Договор {self.id} - {self.client} ({self.tour})"

    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договоры'