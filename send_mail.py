import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':
    send_mail(
        '来自邓锦豪的测试邮件',
        'Hello world',
        '851623837@qq.com',
        ['740493784@qq.com'],
    )

