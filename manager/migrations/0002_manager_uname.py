# Generated by Django 3.2.6 on 2021-09-21 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='uname',
            field=models.CharField(default='', max_length=250),
        ),
    ]
