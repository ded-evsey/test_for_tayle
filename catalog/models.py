from django.db import models
from django.urls import reverse
from transliterate import translit as tt
# Create your models here.


class Section(models.Model):
    name = models.CharField('Наименование раздела', max_length=128)
    img = models.ImageField('Изображение для раздела', upload_to='sections')

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('section_detail', args=[self.id])

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'


class Characteristic(models.Model):
    name = models.CharField('Наименование характеристики', max_length=128)
    value = models.CharField('Значение характеристики', max_length=128)

    def __unicode__(self):
        return self.name, self.value

    class Meta:
        verbose_name = 'Характеристику'
        verbose_name_plural = 'Характеристики'


class Product(models.Model):
    name = models.CharField('Наименование продукта', max_length=128)
    img = models.ImageField('Изображение для продукта', upload_to='product')
    sections = models.ManyToManyField(Section)
    characteristics = models.ManyToManyField(Characteristic)

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('model-detail-view', args=[self.id])

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
