# Generated by Django 3.0.7 on 2022-02-18 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0021_auto_20220219_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responde',
            name='karta_tama',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='karta_tama', to='administrator.Dokumentus'),
        ),
    ]
