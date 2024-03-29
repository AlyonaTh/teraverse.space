# Generated by Django 5.0.1 on 2024-02-17 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_categories_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description2',
            field=models.TextField(null=True, verbose_name='Post text'),
        ),
        migrations.AlterField(
            model_name='post',
            name='description3',
            field=models.TextField(null=True, verbose_name='Post text'),
        ),
        migrations.AlterField(
            model_name='post',
            name='img2',
            field=models.ImageField(null=True, upload_to='images/%Y', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='post',
            name='img3',
            field=models.ImageField(null=True, upload_to='images/%Y', verbose_name='Image'),
        ),
    ]
