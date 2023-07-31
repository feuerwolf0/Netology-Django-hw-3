from django.db import models


class Phone(models.Model):
    name = models.CharField('Название', max_length=32)
    price = models.DecimalField('Цена', decimal_places=2, max_digits=16)
    image = models.CharField('URL изображения', max_length=256)
    release_date = models.DateField('Дата релиза')
    lte_exists = models.BooleanField('Наличие LTE')
    slug = models.SlugField(max_length=64)

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'
