from django.db import models
from django.urls import reverse


class Categories(models.Model):
    """Blog Category"""
    title = models.CharField('Title', max_length=255)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['title']

    def __str__(self):
        return self.title


class Post(models.Model):
    """Post data"""
    title = models.CharField('Post Title', max_length=200)
    author = models.CharField('Author name', max_length=100)
    author_img = models.ImageField('Author image', upload_to='images/author', blank=True, null=True)
    author_about = models.CharField('About author', max_length=500, blank=True, null=True)
    date = models.DateTimeField('Publication date')
    description1 = models.TextField('Post text')
    category = models.ForeignKey(Categories, verbose_name="Category", blank=True, null=True, on_delete=models.DO_NOTHING,
                                 related_name='posts')
    img1 = models.ImageField('Image', upload_to='images/%Y')
    description2 = models.TextField('Post text', null=True, blank=True)
    img2 = models.ImageField('Image', upload_to='images/%Y', null=True, blank=True)
    description3 = models.TextField('Post text', null=True, blank=True)
    img3 = models.ImageField('Image', upload_to='images/%Y', null=True, blank=True)

    def __str__(self):
        return f'{self.title}, {self.author}'

    def get_summary(self):
        words = self.description1.split()
        return f'{" ".join(words[:25])}...'

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class Comments(models.Model):
    email = models.EmailField()
    name = models.CharField('Name', max_length=50)
    body = models.TextField('Comment', max_length=2000)
    post = models.ForeignKey(Post, verbose_name='Post', on_delete=models.CASCADE)
    date = models.DateTimeField('Comment Time', auto_now_add=True)
    parent = models.ForeignKey('self', null=True,blank=True , on_delete=models.CASCADE, related_name='replies')

    def __str__(self):
        return f'{self.name}, {self.post}'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class Likes(models.Model):
    """Likes"""
    ip = models.CharField('IP-address', max_length=100)
    post = models.ForeignKey(Post, verbose_name='Post', on_delete=models.CASCADE)
