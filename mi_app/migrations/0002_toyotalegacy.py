# Generated by Django 5.0.2 on 2024-03-21 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToyotaLegacy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primer_nombre', models.CharField(max_length=15)),
                ('apellido', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefono', models.CharField(max_length=15)),
            ],
        ),
    ]
