# Generated by Django 3.2.6 on 2021-11-04 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0008_auto_20211104_1304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordertable',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='ordertable',
            name='product',
        ),
        migrations.RemoveField(
            model_name='ordertable',
            name='transaction',
        ),
    ]