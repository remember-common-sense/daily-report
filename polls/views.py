from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.template import loader
from django.utils import timezone
from datetime import datetime
from django.core.mail import send_mail
from django.core.mail import EmailMessage

import os

from .models import Choice, Question, Item, Progress1, Progress2, Progress3, Progress4, Team, Risk, Matter, Email, EmailConfig

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Item.objects.filter(is_done=False)

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/dashboard.html', {
            'question': question,
            'error_message': "You didn't select select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def index(request):
    tasks = Item.objects.filter(is_done=False)
    teams = Team.objects.all()
    progress1_list = []
    progress2_list = []
    progress3_list = []
    progress4_list = []
    date_now = datetime.now().date()
    for task in tasks:
        progress1 = Progress1.objects.filter(item=task).order_by('-pub_date').first()
        progress2 = Progress2.objects.filter(item=task).order_by('-pub_date').first()
        progress3 = Progress3.objects.filter(item=task).order_by('-pub_date').first()
        progress4 = Progress4.objects.filter(item=task).order_by('-pub_date').first()
        progress1_list.append(progress1)
        progress2_list.append(progress2)
        progress3_list.append(progress3)
        progress4_list.append(progress4)

    template = loader.get_template('polls/dashboard.html')
    lists = zip(tasks, progress1_list, progress2_list, progress3_list, progress4_list)
    context = {
        'tasks': tasks,
        'teams': teams,
        'progress1_list': progress1_list,
        'progress2_list': progress2_list,
        'progress3_list': progress3_list,
        'progress4_list': progress4_list,
        'date_now': date_now,
        'lists': lists
    }

    return HttpResponse(template.render(context, request))

def dashboard(request):
    teams = Team.objects.all().filter()
    template = loader.get_template('polls/dashboard.html')
    lists = zip(teams)
    context = {
        'lists': lists,
        'teams': teams
    }

    return HttpResponse(template.render(context, request))

def dashboard_id(request, team_id):
    id = team_id
    tasks = Item.objects.filter(team__id=team_id).filter(is_done=False).order_by('system', 'sub_system','pub_date')
    teams = Team.objects.all()
    progress1_list = []
    progress2_list = []
    progress3_list = []
    progress4_list = []
    date_now = datetime.now().date()
    for task in tasks:
        progress1 = Progress1.objects.filter(item=task).order_by('-pub_date').first()
        progress2 = Progress2.objects.filter(item=task).order_by('-pub_date').first()
        progress3 = Progress3.objects.filter(item=task).order_by('-pub_date').first()
        progress4 = Progress4.objects.filter(item=task).order_by('-pub_date').first()
        progress1_list.append(progress1)
        progress2_list.append(progress2)
        progress3_list.append(progress3)
        progress4_list.append(progress4)

    template = loader.get_template('polls/dashboard_id.html')
    lists = zip(tasks, progress1_list, progress2_list, progress3_list, progress4_list)
    context = {
        'team_id': id,
        'tasks': tasks,
        'teams': teams,
        'progress1_list': progress1_list,
        'progress2_list': progress2_list,
        'progress3_list': progress3_list,
        'progress4_list': progress4_list,
        'date_now': date_now,
        'lists': lists
    }

    return HttpResponse(template.render(context, request))

def progress(request):
    teams = Team.objects.all().filter()
    template = loader.get_template('polls/progress.html')
    lists = zip(teams)
    context = {
        'lists': lists,
        'teams': teams
    }

    return HttpResponse(template.render(context, request))

def progress_id(request, team_id):
    date_now = datetime.now().date()
    id = team_id
    teams = Team.objects.all()
    tasks = Item.objects.filter(team__id=team_id).filter(is_done=False)
    risks = Risk.objects.filter(team__id=team_id).filter(pub_date=date_now)
    matters = Matter.objects.filter(team__id=team_id).filter(pub_date=date_now)
    progress1_list = []
    progress1_pre_list = []
    progress2_pre_list = []
    progress3_pre_list = []
    progress4_pre_list = []
    progress2_list = []
    progress3_list = []
    progress4_list = []
    risk_list = []
    matter_list = []
    for risk in risks:
        risk_list.append(risk)
    for matter in matters:
        matter_list.append(matter)
    for task in tasks:
        progress1 = Progress1.objects.filter(item=task).filter(pub_date=date_now)
        if progress1.exists():
            # progress1 = Progress1.objects.filter(item=task).get(pub_date=date_now)
            if(progress1.first().progress != 0):
                progress1_pre = Progress1.objects.filter(item=progress1.first().item).order_by("-pub_date")[1]
            else:
                progress1_pre = progress1.first()
            progress1_list.append(progress1.first())
            progress1_pre_list.append(progress1_pre)

        progress2 = Progress2.objects.filter(item=task).filter(pub_date=date_now)
        if progress2.exists():
            # progress1 = Progress1.objects.filter(item=task).get(pub_date=date_now)
            if (progress2.first().progress != 0):
                progress2_pre = Progress2.objects.filter(item=progress2.first().item).order_by("-pub_date")[1]
            else:
                progress2_pre = progress2.first()
            progress2_list.append(progress2.first())
            progress2_pre_list.append(progress2_pre)

        progress3 = Progress3.objects.filter(item=task).filter(pub_date=date_now)
        if progress3.exists():
            # progress1 = Progress1.objects.filter(item=task).get(pub_date=date_now)
            if (progress3.first().progress != 0):
                progress3_pre = Progress3.objects.filter(item=progress1.first().item).order_by("-pub_date")[1]
            else:
                progress3_pre = progress3.first()
            progress3_list.append(progress3.first())
            progress3_pre_list.append(progress3_pre)

        progress4 = Progress4.objects.filter(item=task).filter(pub_date=date_now)
        if progress4.exists():
            # progress1 = Progress1.objects.filter(item=task).get(pub_date=date_now)
            if (progress4.first().progress != 0):
                progress4_pre = Progress4.objects.filter(item=progress4.first().item).order_by("-pub_date")[1]
            else:
                progress4_pre = progress4.first()
            progress4_list.append(progress4.first())
            progress4_pre_list.append(progress4_pre)

    template = loader.get_template('polls/progress_id.html')
    lists1 = zip(progress1_list, progress1_pre_list)
    lists2 = zip(progress2_list, progress2_pre_list)
    lists3 = zip(progress3_list, progress3_pre_list)
    lists4 = zip(progress4_list, progress4_pre_list)
    context = {
        "lists1": lists1,
        "lists2": lists2,
        "lists3": lists3,
        "lists4": lists4,
        "team_id": id,
        "teams": teams,
        "progress1_list": progress1_list,
        "progress2_list": progress2_list,
        "progress3_list": progress3_list,
        "progress4_list": progress4_list,
        "progress1_pre_list": progress1_pre_list,
        "matters": matter_list,
        "risks": risk_list
    }

    return HttpResponse(template.render(context, request))

def report(request):
    teams = Team.objects.all().filter()
    template = loader.get_template('polls/report.html')
    lists = zip(teams)
    context = {
        'lists': lists,
        'teams': teams
    }

    return HttpResponse(template.render(context, request))

#预览日报
def report_id(request, team_id):
    date_now = datetime.now().date()
    id = team_id
    teams = Team.objects.all()
    email_config = EmailConfig.objects.filter(team__id=team_id).first()
    template = loader.get_template('polls/report_id.html')
    context = {
        "email_config": email_config,
        "date": date_now,
        "teams": teams,
        "team_id": id
    }
    return HttpResponse(template.render(context, request))

#生成日报
def make_report():
    pass

#发送日报
def send_report(request, team_id):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
    date_now = datetime.now().date().__str__()
    email_config = EmailConfig.objects.filter(team__id=team_id).first()
    title = email_config.title + '(' + date_now + ')'
    recipient_list = []     #收件人列表
    cc_list = []   #抄送列表
    recipients = email_config.recipient.all()
    ccs = email_config.cc.all()
    for recipient in recipients:
        recipient_list.append(recipient.__str__())
    for cc in ccs:
        cc_list.append(cc.__str__())

    email = EmailMessage(
        subject=title,
        body='正文',
        from_email='851623837@qq.com',
        to=recipient_list,
        cc=cc_list,
    )

    number = email.send()
    if number == 0 :
        response = "发送失败！"
    else:
        response = "发送成功，共发送" + number.__str__() + "封邮件！"

    return HttpResponse(response)