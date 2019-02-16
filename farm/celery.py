# -*- coding: utf-8 -*-
""" Created by Safa Arıman on 2/16/19 """
from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

__author__ = 'safaariman'


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farm.settings')

app = Celery('farm')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
