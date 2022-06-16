from django.db import models
from django.urls import reverse



# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото', blank=True)
    price = models.CharField(max_length=255, verbose_name='Цена')
    categories = models.ManyToManyField('Category', verbose_name='Категории')
    composition = models.TextField(verbose_name='Состав')
    packaging = models.TextField(verbose_name='Упаковка')
    energy_value = models.TextField(verbose_name='Энеретическая ценность')
    manufacturer = models.TextField(verbose_name='Производитель')
    shelf_life = models.TextField(verbose_name='Срок годности')
    certificates = models.TextField(verbose_name='Сертификаты')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug': self.slug})

    class Meta:
        verbose_name = 'Сырок'
        verbose_name_plural = 'Сырки'
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['price']),
        ]


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']
