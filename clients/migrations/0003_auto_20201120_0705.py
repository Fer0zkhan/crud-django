# Generated by Django 3.1.3 on 2020-11-20 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_auto_20201117_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientusers',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
    ]
