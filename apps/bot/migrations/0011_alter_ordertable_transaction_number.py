# Generated by Django 3.2.6 on 2021-11-04 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0010_alter_ordertable_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordertable',
            name='transaction_number',
            field=models.IntegerField(),
        ),
    ]
