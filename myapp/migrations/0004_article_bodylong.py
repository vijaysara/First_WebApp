# Generated by Django 3.2.6 on 2021-09-17 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20210909_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='bodylong',
            field=models.TextField(default='-'),
        ),
    ]