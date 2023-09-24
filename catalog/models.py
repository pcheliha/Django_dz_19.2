from django.db import models


# Create your models here.
class Product(models.Model):
    p_name = models.CharField(max_length=150, verbose_name='наименование')
    p_description = models.CharField(max_length=150, verbose_name='описание')
    p_image = models.ImageField(upload_to='p_image/')
    p_category = models.ForeignKey('Category', on_delete=models.CASCADE)
    p_price = models.IntegerField(verbose_name='цена')
    p_date_of_creation = models.DateTimeField(auto_now=True, verbose_name='дата создания')
    p_date_of_change = models.DateTimeField(auto_now_add=True, verbose_name='дата изменения')

    def __str__(self):
        return f'{self.p_name} - {self.p_price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Category(models.Model):
    c_name = models.CharField(max_length=150, verbose_name='наименование')
    c_description = models.CharField(max_length=150, verbose_name='описание')


    def __str__(self):
        return f'{self.c_name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'



