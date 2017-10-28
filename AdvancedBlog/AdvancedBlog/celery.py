from __future__ import absolute_import

import os

from celery import Celery

# celery için django default settings dosyasını gösteriyoruz
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AdvancedBlog.settings')

from django.conf import settings

# celery app oluşturuyoruz
app = Celery('AdvancedBlog')

app.config_from_object('django.conf:settings')
# bu fonksiyon sayesinde projemizde her uygulama içerisindeki tasks.py içeriği celery tarafından yorumlanacaktır.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))