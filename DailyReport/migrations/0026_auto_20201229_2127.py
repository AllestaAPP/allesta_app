# Generated by Django 3.1.3 on 2020-12-29 21:27

import DailyReport.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DailyReport', '0025_auto_20201224_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='SIMlockkaijo',
            field=models.IntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999)], verbose_name='SIMロック解除(@200)'),
        ),
        migrations.AddField(
            model_name='item',
            name='hensou',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=5, null=True, validators=[DailyReport.models.check_age], verbose_name='返送関連業務(h) ※0.5h刻みで入力'),
        ),
        migrations.AddField(
            model_name='item',
            name='lanksatei',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=5, null=True, validators=[DailyReport.models.check_age], verbose_name='ランク査定(h) ※0.5h刻みで入力'),
        ),
        migrations.AddField(
            model_name='item',
            name='soukin',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=5, null=True, validators=[DailyReport.models.check_age], verbose_name='送金関連業務(h) ※0.5h刻みで入力'),
        ),
        migrations.AlterField(
            model_name='item',
            name='datanyuuryoku',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=5, null=True, validators=[DailyReport.models.check_age], verbose_name='データ入力・画像登録(h) ※0.5h刻みで入力'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(choices=[('ARS001', 'ARS001'), ('ARS002', 'ARS002'), ('ARS003', 'ARS003'), ('ARS004', 'ARS004'), ('ARS005', 'ARS005'), ('ARS006', 'ARS006'), ('ARS007', 'ARS007'), ('ARS008', 'ARS008'), ('ARS009', 'ARS009'), ('ARS010', 'ARS010'), ('ARS011', 'ARS011'), ('ARS012', 'ARS012'), ('ARS013', 'ARS013'), ('ARS014', 'ARS014'), ('ARS015', 'ARS015'), ('ARS016', 'ARS016'), ('ARS017', 'ARS017'), ('ARS018', 'ARS018'), ('ARS019', 'ARS019'), ('ARS020', 'ARS020'), ('ARS021', 'ARS021'), ('ARS022', 'ARS022'), ('ARS023', 'ARS023'), ('ARS024', 'ARS024'), ('ARS025', 'ARS025'), ('ARS026', 'ARS026'), ('ARS027', 'ARS027'), ('ARS028', 'ARS028'), ('ARS029', 'ARS029'), ('ARS030', 'ARS030')], max_length=20, verbose_name='名前'),
        ),
        migrations.AlterField(
            model_name='item',
            name='picking',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=5, null=True, validators=[DailyReport.models.check_age], verbose_name='搬出・ピッキング(h) ※0.5h刻みで入力'),
        ),
        migrations.AlterField(
            model_name='item',
            name='takuhaikaikon',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=5, null=True, validators=[DailyReport.models.check_age], verbose_name='宅配開梱(h) ※0.5h刻みで入力'),
        ),
        migrations.AlterField(
            model_name='item',
            name='tsutaya',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=5, null=True, validators=[DailyReport.models.check_age], verbose_name='TSUTAYA関連(h) ※0.5h刻みで入力'),
        ),
    ]
