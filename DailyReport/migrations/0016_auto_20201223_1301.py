# Generated by Django 3.1.3 on 2020-12-23 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DailyReport', '0015_auto_20201221_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='tmp',
            field=models.IntegerField(blank=True, default=0, editable=False, null=True, verbose_name='仮登録'),
        ),
    ]