# Generated by Django 5.1.2 on 2024-11-25 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('codigo', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('apellidom', models.CharField(max_length=100)),
                ('cuenta', models.CharField(max_length=100)),
                ('apellidop', models.CharField(max_length=100)),
            ],
        ),
    ]