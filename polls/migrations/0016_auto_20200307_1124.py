# Generated by Django 2.2 on 2020-03-07 03:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_auto_20200307_0939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='姓名')),
                ('address', models.CharField(max_length=100, verbose_name='邮箱地址')),
            ],
            options={
                'verbose_name': '邮箱',
                'verbose_name_plural': '邮箱',
            },
        ),
        migrations.AlterField(
            model_name='item',
            name='pub_date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 3, 7, 3, 24, 10, 653176, tzinfo=utc), verbose_name='上线日期'),
        ),
        migrations.AlterField(
            model_name='matter',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 7, 3, 24, 10, 672193, tzinfo=utc), verbose_name='更新日期'),
        ),
        migrations.AlterField(
            model_name='otherwork',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 7, 3, 24, 10, 671192, tzinfo=utc), verbose_name='更新日期'),
        ),
        migrations.AlterField(
            model_name='progress1',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 7, 3, 24, 10, 670192, tzinfo=utc), verbose_name='更新日期'),
        ),
        migrations.AlterField(
            model_name='progress2',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 7, 3, 24, 10, 670192, tzinfo=utc), verbose_name='更新日期'),
        ),
        migrations.AlterField(
            model_name='progress3',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 7, 3, 24, 10, 670192, tzinfo=utc), verbose_name='更新日期'),
        ),
        migrations.AlterField(
            model_name='progress4',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 7, 3, 24, 10, 671192, tzinfo=utc), verbose_name='更新日期'),
        ),
        migrations.AlterField(
            model_name='risk',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 7, 3, 24, 10, 671192, tzinfo=utc), verbose_name='更新日期'),
        ),
    ]
