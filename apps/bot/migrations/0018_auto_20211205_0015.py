# Generated by Django 3.2.6 on 2021-12-04 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0017_alter_shop_company_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordertable',
            name='message',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='ordertable',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
