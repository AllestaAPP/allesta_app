# Generated by Django 3.1.3 on 2020-12-24 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DailyReport', '0022_auto_20201224_1518'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': '日報', 'verbose_name_plural': '日報'},
        ),
        migrations.AlterField(
            model_name='item',
            name='tmp',
            field=models.BooleanField(verbose_name='一時保存'),
        ),
    ]
