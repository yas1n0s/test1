from django.db import models

# Create your models here.

from django.db import models

class SiteInfo(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название сайта"
    )
    description = models.TextField(
        verbose_name="Краткое описание"
    )
    logo = models.ImageField(
        upload_to="site_logo/",
        verbose_name="Логотип сайта"
    )
    phone_number = models.CharField(
        max_length=20,
        verbose_name="Номер телефона"
    )
    email = models.EmailField(
        verbose_name="Электронная почта"
    )
    address = models.CharField(
        max_length=255,
        verbose_name="Физический адрес"
    )

    class Meta:
        verbose_name = "Информация о сайте"
        verbose_name_plural = "Информация о сайте"

    def __str__(self):
        return self.title
