# Generated by Django 3.2.6 on 2021-09-02 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foody', '0008_veg_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='veg',
            name='quantity',
        ),
    ]
