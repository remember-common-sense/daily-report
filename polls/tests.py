import datetime
import os

from django.core.mail import send_mail
from django.utils import timezone
from django.test import TestCase
from .models import Question

class QuestionMethodTests(TestCase):
    # def test_was_published_recently_with_future_question(self):
    #     """
    #     在将来发布的问卷应该返回False
    #     """
    #     time = timezone.now() + datetime.timedelta(days=30)
    #     future_question = Question(pub_date=time)
    #     self.assertIs(future_question.was_published_recently(), False)

    def send_mail(self):
        send_mail(
            '来自邓锦豪的测试邮件',
            'Hello world',
            '851623837@qq.com',
            ['740493784@qq.com'],
        )