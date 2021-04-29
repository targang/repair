from django.db import models


class Order(models.Model):
    class Meta:
        verbose_name = "заявка"
        verbose_name_plural = "заявки"

    name = models.CharField(max_length=50, null=False, blank=False, verbose_name="Имя")
    phone = models.CharField(
        max_length=100, null=False, blank=False, verbose_name="Номер телефона"
    )
    message = models.TextField(verbose_name="Сообщение")

    def publish(self):
        self.save()

    def __str__(self) -> str:
        return f"Заявка №{self.id}"

