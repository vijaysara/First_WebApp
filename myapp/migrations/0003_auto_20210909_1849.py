# Generated by Django 3.2.6 on 2021-09-10 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20210909_0849'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='picname2',
            field=models.TextField(default='_'),
        ),
        migrations.AddField(
            model_name='article',
            name='picurl2',
            field=models.TextField(default='_'),
        ),
    ]