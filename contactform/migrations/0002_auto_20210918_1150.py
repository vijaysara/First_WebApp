# Generated by Django 3.2.6 on 2021-09-18 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactform', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='date',
            field=models.CharField(default='-', max_length=250),
        ),
        migrations.AddField(
            model_name='contactform',
            name='time',
            field=models.CharField(default='-', max_length=250),
        ),
    ]
