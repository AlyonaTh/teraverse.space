from django.db import models


class Contact(models.Model):
    """Contact us"""
    name = models.CharField('Name', max_length=255)
    subject = models.CharField('Subject', max_length=255)
    email = models.EmailField()
    date = models.DateTimeField('Contact Time', auto_now_add=True)
    message = models.TextField('Message')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Contact'