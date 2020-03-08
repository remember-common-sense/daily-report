# Generated by Django 2.2 on 2020-01-19 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='姓名')),
            ],
            options={
                'verbose_name': '开发人员',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=200, verbose_name='上线功能点')),
                ('sub_task', models.CharField(blank=True, max_length=200, verbose_name='子任务分解')),
                ('comment', models.CharField(blank=True, max_length=200, verbose_name='备注')),
                ('developer', models.ManyToManyField(to='polls.Developer')),
            ],
            options={
                'verbose_name': '测试任务',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=200, verbose_name='角色名称')),
            ],
            options={
                'verbose_name': '角色',
            },
        ),
        migrations.CreateModel(
            name='SubSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_system_name', models.CharField(max_length=200, verbose_name='子系统名称')),
            ],
            options={
                'verbose_name': '子系统',
            },
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system_name', models.CharField(max_length=200, verbose_name='项目名称')),
            ],
            options={
                'verbose_name': '项目',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=200, verbose_name='团队名称')),
            ],
            options={
                'verbose_name': '所属团队',
            },
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': '问题', 'verbose_name_plural': '问题'},
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name='发布日期'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=200, verbose_name='问题内容'),
        ),
        migrations.CreateModel(
            name='Tester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='姓名')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Role')),
            ],
            options={
                'verbose_name': '测试人员',
            },
        ),
        migrations.CreateModel(
            name='Progress4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progress', models.IntegerField(max_length=100, verbose_name='进度(%)')),
                ('pub_date', models.DateField(verbose_name='更新日期')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Item')),
            ],
            options={
                'verbose_name': '测试报告编写进度(%)',
            },
        ),
        migrations.CreateModel(
            name='Progress3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progress', models.IntegerField(max_length=100, verbose_name='进度(%)')),
                ('pub_date', models.DateField(verbose_name='更新日期')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Item')),
            ],
            options={
                'verbose_name': '测试用例执行进度(%)',
            },
        ),
        migrations.CreateModel(
            name='Progress2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progress', models.IntegerField(max_length=100, verbose_name='进度(%)')),
                ('pub_date', models.DateField(verbose_name='更新日期')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Item')),
            ],
            options={
                'verbose_name': '测试用例编写进度(%)',
            },
        ),
        migrations.CreateModel(
            name='Progress1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progress', models.IntegerField(max_length=100, verbose_name='进度(%)')),
                ('pub_date', models.DateField(verbose_name='更新日期')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Item')),
            ],
            options={
                'verbose_name': '需求理解进度(%)',
            },
        ),
        migrations.AddField(
            model_name='item',
            name='sub_system',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.SubSystem'),
        ),
        migrations.AddField(
            model_name='item',
            name='system',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.System'),
        ),
        migrations.AddField(
            model_name='item',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Team'),
        ),
        migrations.AddField(
            model_name='item',
            name='tester',
            field=models.ManyToManyField(to='polls.Tester'),
        ),
        migrations.AddField(
            model_name='developer',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Role'),
        ),
    ]
