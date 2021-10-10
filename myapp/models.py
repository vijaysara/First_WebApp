import django.db.models
from django.db import models




# Create your models here.
class article(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    bodylong = models.TextField(default='-')
    fb = models.CharField(default='-', max_length=250)
    tw = models.CharField(default='-', max_length=250)
    yt = models.CharField(default='-', max_length=250)
    ph = models.CharField(default='-', max_length=250)
    picurl = models.TextField(default='_')
    picname = models.TextField(default='_')
    picurl2 = models.TextField(default='_')
    picname2 = models.TextField(default='_')

    def __str__(self):
        return self.title+' | ' +str(self.pk)
