# Generated by Django 5.0.1 on 2024-02-21 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_categories_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img1',
            field=models.ImageField(blank=True, null=True, upload_to='images/shop', verbose_name='Product image 1'),
        ),
        migrations.AddField(
            model_name='product',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to='images/shop', verbose_name='Product image 2'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=255, verbose_name='Product description'),
        ),
    ]
