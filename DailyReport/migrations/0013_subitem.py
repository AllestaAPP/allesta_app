# Generated by Django 3.1.3 on 2020-12-18 14:57

import DailyReport.models
import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('DailyReport', '0012_auto_20201123_2000'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('作業者1', '作業者1'), ('作業者2', '作業者2'), ('作業者3', '作業者3'), ('作業者4', '作業者4'), ('作業者5', '作業者5'), ('作業者6', '作業者6'), ('作業者7', '作業者7'), ('作業者8', '作業者8'), ('作業者9', '作業者9'), ('作業者10', '作業者10'), ('作業者11', '作業者11'), ('作業者12', '作業者12'), ('作業者13', '作業者13'), ('作業者14', '作業者14'), ('作業者15', '作業者15'), ('作業者16', '作業者16'), ('作業者17', '作業者17'), ('作業者18', '作業者18'), ('作業者19', '作業者19'), ('作業者20', '作業者20'), ('作業者21', '作業者21'), ('作業者22', '作業者22'), ('作業者23', '作業者23'), ('作業者24', '作業者24'), ('作業者25', '作業者25'), ('作業者26', '作業者26'), ('作業者27', '作業者27'), ('作業者28', '作業者28'), ('作業者29', '作業者29'), ('作業者30', '作業者30')], max_length=20, verbose_name='名前')),
                ('takuhaikenpin', models.IntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(300)], verbose_name='宅配検品(@400)')),
                ('sonotakenpin', models.IntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999)], verbose_name='その他検品(@200)')),
                ('nyuukosyouhinka', models.IntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999)], verbose_name='入庫商品化(@200)')),
                ('shiiresyouhinka', models.IntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5000)], verbose_name='仕入商品化(@100)')),
                ('cleaning', models.IntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5000)], verbose_name='クリーニング(@50)')),
                ('dataerase', models.IntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999)], verbose_name='データイレース(@50)')),
                ('shiirePC', models.IntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999)], verbose_name='仕入PC(@1000)')),
                ('tsutaya', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True, validators=[DailyReport.models.check_age], verbose_name='TSUTAYA関連(h) ※0.5h刻みで入力')),
                ('takuhaikaikon', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True, validators=[DailyReport.models.check_age], verbose_name='宅配開梱(h) ※0.5h刻みで入力')),
                ('picking', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True, validators=[DailyReport.models.check_age], verbose_name='搬出・ピッキング(h) ※0.5h刻みで入力')),
                ('datanyuuryoku', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True, validators=[DailyReport.models.check_age], verbose_name='データ入力・画像登録(h) ※0.5h刻みで入力')),
                ('memo', models.TextField(blank=True, max_length=300, null=True, verbose_name='備考')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='登録日')),
            ],
        ),
    ]
