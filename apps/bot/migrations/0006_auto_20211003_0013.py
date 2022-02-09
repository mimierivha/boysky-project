# Generated by Django 3.1.4 on 2021-10-02 22:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0005_auto_20210810_1422'),
    ]

    operations = [
        migrations.CreateModel(
            name='FindTaxi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=30)),
                ('current_location', models.CharField(max_length=30)),
                ('destination', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='activated',
            field=models.CharField(default=datetime.datetime(2021, 10, 3, 0, 13, 7, 779747), max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='subrscibed',
            field=models.CharField(default='hy', max_length=16),
            preserve_default=False,
        ),
    ]
