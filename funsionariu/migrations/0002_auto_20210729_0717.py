# Generated by Django 3.0.7 on 2021-07-29 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funsionariu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vogal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vogal', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='diresaun',
            name='vogal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='funsionariu.Vogal'),
        ),
        migrations.AddField(
            model_name='funsionariu',
            name='vogal',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='funsionariu.Vogal'),
        ),
    ]
