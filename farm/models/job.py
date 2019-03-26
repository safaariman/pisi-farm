# -*- coding: utf-8 -*-
""" Created by Safa Arıman on 2/16/19 """
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_celery_results.models import TaskResult

from farm.base.model import Model
from farm.models import Event

__author__ = 'safaariman'


class Job(Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    task = models.ForeignKey(TaskResult, null=True, to_field='task_id', on_delete=models.SET_NULL)

    class Meta:
        db_table = 'job'
        verbose_name = _('Job')
        verbose_name_plural = _('Jobs')
