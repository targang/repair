from django.db import models


class GalleryImage(models.Model):
    class Meta:
        verbose_name = "фото"
        verbose_name_plural = "фотографии"

    alt = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Подпись"
    )
    image = models.ImageField(
        blank=False, upload_to="gallery/", verbose_name="Изображение"
    )

    def publish(self):
        self.save()


    def __str__(self) -> str:
        return f"{self.image}"


class Service(models.Model):
    class Meta:
        verbose_name = "услуга"
        verbose_name_plural = "услуги"

    name = models.CharField(
        max_length=100, null=False, blank=False, verbose_name="Название услуги"
    )
    description = models.TextField(
        max_length=700, null=False, blank=False, verbose_name="Описание услуги"
    )
    price = models.CharField(
        max_length=100, null=False, blank=False, verbose_name="Цена услуги"
    )

    def publish(self):
        self.save()

    def __str__(self) -> str:
        return f"{self.name}"
