# Generated by Django 5.0.1 on 2024-02-17 09:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_description2_alter_post_description3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='blog.comments'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author_about',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='About author'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/author', verbose_name='Author image'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='blog.categories', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='description2',
            field=models.TextField(blank=True, null=True, verbose_name='Post text'),
        ),
        migrations.AlterField(
            model_name='post',
            name='description3',
            field=models.TextField(blank=True, null=True, verbose_name='Post text'),
        ),
        migrations.AlterField(
            model_name='post',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to='images/%Y', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='post',
            name='img3',
            field=models.ImageField(blank=True, null=True, upload_to='images/%Y', verbose_name='Image'),
        ),
    ]