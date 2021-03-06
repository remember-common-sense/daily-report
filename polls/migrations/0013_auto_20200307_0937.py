# Generated by Django 2.2 on 2020-03-07 01:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20200307_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='pub_date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 3, 7, 1, 37, 54, 367983, tzinfo=utc), verbose_name='上线日期'),
        ),
        migrations.AlterField(
            model_name='matter',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 7, 1, 37, 54, 400013, tzinfo=utc), verbose_name='更新日期'),
        ),
        migrations.AlterField(
            model_name='otherwork',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 7, 1, 37, 54, 398011, tzinfo=utc), verbose_name='更新日期'),
        ),
        migrations.AlterField(
            model_name='progress1',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 7, 1, 37, 54, 394007, tzinfo=utc), verbose_name='更新日期'),
        ),
        migrations.AlterField(
            model_name='progress2',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 7, 1, 37, 54, 395008, tzinfo=utc), verbose_name='更新日期'),
        ),
        migrations.AlterField(
            model_name='progress3',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 7, 1, 37, 54, 396009, tzinfo=utc), verbose_name='更新日期'),
        ),
        migrations.AlterField(
            model_name='progress4',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 7, 1, 37, 54, 397010, tzinfo=utc), verbose_name='更新日期'),
        ),
        migrations.AlterField(
            model_name='risk',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 7, 1, 37, 54, 399012, tzinfo=utc), verbose_name='更新日期'),
        ),
    ]
