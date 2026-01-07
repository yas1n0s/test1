from django.db import models

# Create your models here.
from django.db import models

class Settings(models.Model):
    site_name = models.CharField(max_length=255, verbose_name="Название сайта")
    contact_email = models.EmailField(verbose_name="Электронная почта")

    class Meta:
        verbose_name = "Настройки"
        verbose_name_plural = "Настройки"

    def __str__(self):
        return self.site_name



