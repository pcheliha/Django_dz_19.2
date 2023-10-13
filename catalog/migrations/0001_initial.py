# Generated by Django 4.2.5 on 2023-09-24 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=150, verbose_name='наименование')),
                ('c_description', models.CharField(max_length=150, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=150, verbose_name='наименование')),
                ('p_description', models.CharField(max_length=150, verbose_name='описание')),
                ('p_image', models.ImageField(upload_to='p_image/')),
                ('p_price', models.IntegerField(verbose_name='цена')),
                ('p_date_of_creation', models.DateTimeField(verbose_name='дата создания')),
                ('p_date_of_change', models.DateTimeField(verbose_name='дата изменения')),
                ('p_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
            },
        ),
    ]