from django.db import models

# Create your models here.
class News(models.Model):
    name = models.CharField(max_length=250)
    summary = models.TextField()
    body = models.TextField(default='_')
    date = models.DateField()
    picname = models.TextField()
    picurl = models.TextField(default='_')
    author = models.CharField(max_length=250, default='_')
    catname =models.CharField(max_length=250, default='_')
    catid = models.IntegerField(default=0)
    ocatid = models.IntegerField(default=0)
    show = models.IntegerField(default=0)
    tags = models.TextField(default='_')


    def __str__(self):
        return self.name + '|' + str(self.pk)
