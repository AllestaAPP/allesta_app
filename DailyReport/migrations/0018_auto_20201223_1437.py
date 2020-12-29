# Generated by Django 3.1.3 on 2020-12-23 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DailyReport', '0017_auto_20201223_1307'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SubItem',
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'アイテム', 'verbose_name_plural': 'アイテム'},
        ),
        migrations.RemoveField(
            model_name='item',
            name='sex',
        ),
        migrations.AlterField(
            model_name='item',
            name='tmp',
            field=models.IntegerField(blank=True, choices=[(1, 1)], default=0, null=True, verbose_name='仮登録'),
        ),
    ]