# Generated by Django 4.0.6 on 2022-08-01 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_rename_address1_order_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='sector',
        ),
    ]
