from django.db import models


class Categories(models.Model):
    """Shop Category"""
    title = models.CharField('Title', max_length=255)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['title']

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField('Product Name', max_length=100)
    description = models.TextField('Product description', max_length=255)
    img = models.ImageField('Product image', upload_to='images/shop')
    img1 = models.ImageField('Product image 1', upload_to='images/shop', blank=True, null=True)
    img2 = models.ImageField('Product image 2', upload_to='images/shop', blank=True, null=True)
    link = models.CharField('Affiliate link', max_length=200)
    category = models.ForeignKey(Categories, verbose_name="Category", blank=True, null=True,
                                 on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.title}, {self.description}'

    class Meta:
        verbose_name = 'Product'
