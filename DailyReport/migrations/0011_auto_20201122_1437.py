# Generated by Django 3.1.3 on 2020-11-22 14:37

import DailyReport.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DailyReport', '0010_auto_20201122_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='datanyuuryoku',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True, validators=[DailyReport.models.check_age], verbose_name='データ入力・画像登録(h)※0.5h刻みで入力'),
        ),
        migrations.AlterField(
            model_name='item',
            name='takuhaikaikon',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True, validators=[DailyReport.models.check_age], verbose_name='宅配開梱(h)※0.5h刻みで入力'),
        ),
        migrations.AlterField(
            model_name='item',
            name='tsutaya',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True, validators=[DailyReport.models.check_age], verbose_name='TSUTAYA関連(h)※0.5h刻みで入力'),
        ),
    ]
