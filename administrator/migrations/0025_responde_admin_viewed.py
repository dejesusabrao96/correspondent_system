# Generated by Django 3.0.7 on 2022-02-19 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0024_auto_20220219_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='responde',
            name='admin_viewed',
            field=models.BooleanField(default=False),
        ),
    ]