# Generated by Django 3.2.6 on 2021-09-02 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foody', '0012_veg_order_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='veg_order',
            name='total',
        ),
    ]
