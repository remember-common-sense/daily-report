import datetime

from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Question(models.Model):
    class Meta:
        verbose_name = '问题'
        verbose_name_plural = '问题'

    question_text = models.CharField(max_length=200, verbose_name='问题内容')
    pub_date = models.DateTimeField('发布日期')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def get_question_text(self):
        return self.question_text

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    get_question_text.short_description = '问题内容'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

#团队
class Team(models.Model):
    class Meta:
        verbose_name='所属团队'
        verbose_name_plural = '所属团队'

    team_name = models.CharField(max_length=200, verbose_name='团队名称')

    def __str__(self):
        return self.team_name


#系统
class System(models.Model):
    class Meta:
        verbose_name='项目'
        verbose_name_plural = '项目'

    system_name = models.CharField(max_length=200, verbose_name='项目名称')

    def __str__(self):
        return self.system_name


#子系统
class SubSystem(models.Model):
    class Meta:
        verbose_name='子系统'
        verbose_name_plural = '子系统'

    sub_system_name = models.CharField(max_length=200, verbose_name='子系统名称')

    def __str__(self):
        return self.sub_system_name


#角色
class Role(models.Model):
    class Meta:
        verbose_name = '角色'
        verbose_name_plural = '角色'
    role_name = models.CharField(max_length=200, verbose_name='角色名称')

    def __str__(self):
        return self.role_name


#开发人员
class Developer(models.Model):
    class Meta:
        verbose_name = '开发人员'
        verbose_name_plural = '开发人员'

    name = models.CharField(max_length=200, verbose_name='姓名')
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

#测试人员
class Tester(models.Model):
    class Meta:
        verbose_name = '测试人员'
        verbose_name_plural = '测试人员'

    name = models.CharField(max_length=200, verbose_name='姓名')
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


#任务项
class Item(models.Model):
    class Meta:
        verbose_name='测试任务'
        verbose_name_plural = '测试任务'

    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='所属团队')
    system = models.ForeignKey(System, on_delete=models.CASCADE, verbose_name='项目')
    sub_system = models.ForeignKey(SubSystem, on_delete=models.CASCADE, verbose_name='子系统')
    task = models.CharField(max_length=200, verbose_name='上线功能点')
    sub_task = models.CharField(max_length=200, blank=True, verbose_name='子任务分解')
    developer = models.ManyToManyField(Developer, verbose_name='开发人员')
    tester = models.ManyToManyField(Tester, verbose_name='测试人员')
    comment = models.CharField(max_length=200, blank=True, verbose_name='备注')
    pub_date = models.DateField('上线日期', default=timezone.now(), blank=True)
    is_done = models.BooleanField(default=False, verbose_name='完成情况')

    def __str__(self):
        return self.task + ' ' + self.sub_task


#需求理解进度
class Progress1(models.Model):
    class Meta:
        verbose_name='需求理解进度(%)'
        verbose_name_plural = '需求理解进度(%)'

    progress = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)], verbose_name='进度(%)')
    pub_date = models.DateField('更新日期', default=timezone.now())
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.progress)


#测试用例编写进度
class Progress2(models.Model):
    class Meta:
        verbose_name='测试用例编写进度(%)'
        verbose_name_plural = '测试用例编写进度(%)'

    progress = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)], verbose_name='进度(%)')
    pub_date = models.DateField('更新日期', default=timezone.now())
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.progress)

#测试用例执行进度
class Progress3(models.Model):
    class Meta:
        verbose_name='测试用例执行进度(%)'
        verbose_name_plural = '测试用例执行进度(%)'

    progress = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)], verbose_name='进度(%)')
    pub_date = models.DateField('更新日期', default=timezone.now())
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.progress)


#测试报告编写进度
class Progress4(models.Model):
    class Meta:
        verbose_name='测试报告编写进度(%)'
        verbose_name_plural = '测试报告编写进度(%)'

    progress = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)], verbose_name='进度(%)')
    pub_date = models.DateField('更新日期', default=timezone.now())
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.progress)

#其他工作
class OtherWork(models.Model):
    class Meta:
        verbose_name = '其他工作'
        verbose_name_plural = '其他工作'

    content = models.TextField(verbose_name='其他工作')
    pub_date = models.DateField('更新日期', default=timezone.now())
    tester = models.ForeignKey(Tester, on_delete=models.CASCADE, verbose_name='测试人员')

#存在的风险
class Risk(models.Model):
    class Meta:
        verbose_name = '存在的风险'
        verbose_name_plural = '存在的风险'

    content = models.TextField(verbose_name='存在的风险')
    pub_date = models.DateField('更新日期', default=timezone.now())
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='所属团队')

#协调事项
class Matter(models.Model):
    class Meta:
        verbose_name = '协调事项'
        verbose_name_plural = '协调事项'

    content = models.TextField(verbose_name='协调事项')
    pub_date = models.DateField('更新日期', default=timezone.now())
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='所属团队')

#邮箱信息
class Email(models.Model):
    class Meta:
        verbose_name = '邮箱'
        verbose_name_plural = '邮箱'

    name = models.CharField(max_length=100, verbose_name="姓名")
    address = models.CharField(max_length=100, verbose_name="邮箱地址")

    def __str__(self):
        return self.name + "<" + self.address + ">"

#发送邮件配置
class EmailConfig(models.Model):
    class Meta:
        verbose_name = '邮箱配置'
        verbose_name_plural = '邮箱配置'

    title = models.CharField(max_length=100, verbose_name="主题")
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name="团队")
    recipient = models.ManyToManyField(Email, verbose_name="收件人", related_name="recipient")
    cc = models.ManyToManyField(Email, verbose_name="抄送", related_name="cc")
