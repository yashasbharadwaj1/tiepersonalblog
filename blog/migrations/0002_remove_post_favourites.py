# Generated by Django 4.1.1 on 2022-09-26 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='favourites',
        ),
    ]
