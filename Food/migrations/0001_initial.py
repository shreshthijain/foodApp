# Generated by Django 5.2.3 on 2025-07-21 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('item_description', models.CharField(max_length=500)),
                ('item_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('item_image', models.ImageField(blank=True, null=True, upload_to='item_images/')),
                ('item_category', models.CharField(max_length=50)),
                ('item_available', models.BooleanField(default=True)),
            ],
        ),
    ]
