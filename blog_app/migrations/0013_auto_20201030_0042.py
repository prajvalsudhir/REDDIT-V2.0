# Generated by Django 3.0.2 on 2020-10-29 19:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_app', '0012_auto_20200924_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='user_like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='like',
        ),
    ]
