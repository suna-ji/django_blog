# Generated by Django 2.2.7 on 2020-02-10 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200210_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='img/basic.png', upload_to='img/', verbose_name='Image of User'),
        ),
    ]
