# Generated by Django 3.0.7 on 2022-02-19 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0025_responde_admin_viewed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responde',
            name='file_respond',
            field=models.FileField(max_length=200, null=True, upload_to='responde/'),
        ),
    ]
