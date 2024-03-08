from django.db import models


class About(models.Model):
    """About us"""
    title = models.CharField('About title', max_length=100)
    text = models.TextField('About text')
    img = models.ImageField('About Image', upload_to='image/about')

    def __str__(self):
        return f'{self.title}, {self.text}'

    class Meta:
        verbose_name = 'About'