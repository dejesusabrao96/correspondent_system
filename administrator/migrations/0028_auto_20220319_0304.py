# Generated by Django 3.0.7 on 2022-03-18 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0027_auto_20220318_2211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dokumentusaiinterna',
            name='aprova',
        ),
        migrations.AddField(
            model_name='dokumentusaiinterna',
            name='deskrisaun',
            field=models.TextField(blank=True, null=True),
        ),
    ]