# Generated by Django 3.0.7 on 2021-11-23 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0005_auto_20211115_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryDocSai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_code', models.CharField(max_length=10, verbose_name='Kodigu Kategoria')),
                ('cat_name', models.CharField(max_length=10, verbose_name='Kodigu Kategoria')),
            ],
            options={
                'verbose_name_plural': 'Category Karta Sai',
            },
        ),
    ]