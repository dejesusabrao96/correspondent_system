# Generated by Django 3.0.7 on 2022-02-08 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0016_auto_20220206_0733'),
    ]

    operations = [
        migrations.AddField(
            model_name='dokumentusai',
            name='diretor_viewed',
            field=models.BooleanField(default=False),
        ),
    ]