# Generated by Django 3.0.7 on 2022-03-19 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0028_auto_20220319_0304'),
    ]

    operations = [
        migrations.AddField(
            model_name='dokumentusaiinterna',
            name='president_despacho',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]