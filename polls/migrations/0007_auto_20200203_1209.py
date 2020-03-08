# Generated by Django 2.2 on 2020-02-03 04:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20200120_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='pub_date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 2, 3, 4, 9, 28, 300311, tzinfo=utc), verbose_name='上线日期'),
        ),
        migrations.AlterField(
            model_name='progress1',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 2, 3, 4, 9, 28, 328338, tzinfo=utc), verbose_name='更新日期'),
        ),
        migrations.AlterField(
            model_name='progress2',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 2, 3, 4, 9, 28, 328338, tzinfo=utc), verbose_name='更新日期'),
        ),
        migrations.AlterField(
            model_name='progress3',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 2, 3, 4, 9, 28, 329339, tzinfo=utc), verbose_name='更新日期'),
        ),
        migrations.AlterField(
            model_name='progress4',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 2, 3, 4, 9, 28, 329339, tzinfo=utc), verbose_name='更新日期'),
        ),
    ]