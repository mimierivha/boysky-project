# Generated by Django 3.2.6 on 2021-12-04 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0019_auto_20211205_0104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='shop',
        ),
        migrations.AddField(
            model_name='product',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bot.company'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shop',
            name='company_id',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='bot.company'),
        ),
    ]
