# Generated by Django 3.0.7 on 2021-12-11 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0002_auto_20211211_1805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='informacion',
        ),
    ]
