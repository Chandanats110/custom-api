# Generated by Django 5.1.1 on 2024-11-26 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customapiapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='trains',
            new_name='train',
        ),
    ]