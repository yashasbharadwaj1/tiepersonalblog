# Generated by Django 4.1.1 on 2022-09-30 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_likes_post_likes_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='posts/default.jpg', upload_to='posts'),
        ),
    ]
