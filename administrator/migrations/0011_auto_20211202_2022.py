# Generated by Django 3.0.7 on 2021-12-03 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0010_responde'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dokumentusai',
            old_name='president_despacho',
            new_name='president_despacho_diresaun',
        ),
    ]