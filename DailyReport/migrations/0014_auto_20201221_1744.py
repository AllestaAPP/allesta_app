# Generated by Django 3.1.3 on 2020-12-21 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DailyReport', '0013_subitem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={},
        ),
        migrations.AddField(
            model_name='item',
            name='tmp',
            field=models.IntegerField(blank=True, default=0, max_length=1, null=True, verbose_name='仮登録'),
        ),
    ]
