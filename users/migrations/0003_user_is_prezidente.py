# Generated by Django 3.0.7 on 2021-07-29 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210729_0600'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_prezidente',
            field=models.BooleanField(default=False),
        ),
    ]