# Generated by Django 4.2 on 2023-05-12 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_basket'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукти'},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'Категорія', 'verbose_name_plural': 'Категорії'},
        ),
    ]
