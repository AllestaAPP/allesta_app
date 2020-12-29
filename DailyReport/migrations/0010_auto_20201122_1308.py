# Generated by Django 3.1.3 on 2020-11-22 13:08

import DailyReport.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DailyReport', '0009_auto_20201122_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='picking',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True, validators=[DailyReport.models.check_age], verbose_name='搬出・ピッキング(h)※0.5h刻みで入力'),
        ),
    ]
