# Generated by Django 5.0.2 on 2024-04-15 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_app', '0002_toyotalegacy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('text', models.CharField(max_length=100)),
            ],
        ),
    ]
