# Generated by Django 2.2 on 2020-03-06 15:42

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20200306_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='otherwork',
            name='tester',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='polls.Tester', verbose_name='测试人员'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='pub_date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 3, 6, 15, 41, 5, 644031, tzinfo=utc), verbose_name='上线日期'),
        ),
        migrations.AlterField(
            model_name='matter',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 6, 15, 41, 5, 662047, tzinfo=utc), verbose_name='更新日期'),
        ),
        migrations.AlterField(
            model_name='otherwork',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 6, 15, 41, 5, 662047, tzinfo=utc), verbose_name='更新日期'),
        ),
        migrations.AlterField(
            model_name='progress1',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 6, 15, 41, 5, 660045, tzinfo=utc), verbose_name='更新日期'),
        ),
        migrations.AlterField(
            model_name='progress2',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 6, 15, 41, 5, 661047, tzinfo=utc), verbose_name='更新日期'),
        ),
        migrations.AlterField(
            model_name='progress3',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 6, 15, 41, 5, 661047, tzinfo=utc), verbose_name='更新日期'),
        ),
        migrations.AlterField(
            model_name='progress4',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 6, 15, 41, 5, 661047, tzinfo=utc), verbose_name='更新日期'),
        ),
        migrations.AlterField(
            model_name='risk',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 6, 15, 41, 5, 662047, tzinfo=utc), verbose_name='更新日期'),
        ),
    ]
