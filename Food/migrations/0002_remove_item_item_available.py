# Generated by Django 5.2.3 on 2025-07-24 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Food', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='item_available',
        ),
    ]
