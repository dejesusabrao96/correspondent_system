# Generated by Django 3.0.7 on 2021-07-01 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Diresaun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigu_diresaun', models.CharField(max_length=20, null=True, unique=True)),
                ('diresaun', models.CharField(max_length=100, null=True)),
                ('hashed', models.CharField(max_length=32, null=True)),
            ],
            options={
                'verbose_name_plural': 'Diresaun',
            },
        ),
        migrations.CreateModel(
            name='Kargu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigu_kargu', models.CharField(max_length=20, null=True, unique=True)),
                ('kargu', models.CharField(max_length=100, null=True)),
                ('hashed', models.CharField(max_length=32, null=True)),
                ('diresaun', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='funsionariu.Diresaun')),
            ],
            options={
                'verbose_name_plural': 'Kargo',
            },
        ),
        migrations.CreateModel(
            name='Funsionariu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naran_funsionariu', models.CharField(max_length=100, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('hashed', models.CharField(max_length=32, null=True)),
                ('foto', models.ImageField(upload_to='picture')),
                ('kargu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='funsionariu.Kargu')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Funsionariu',
            },
        ),
    ]
