# -*- coding: utf-8 -*-
""" Created by Safa Arıman on 2/16/19 """
from django.db import models
from django.utils.translation import ugettext_lazy as _

from farm.base.model import Model

__author__ = 'safaariman'


class Job(Model):
    started_at = models.DateTimeField(verbose_name=_('Started At'), null=True, blank=True)
    finished_at = models.DateTimeField(verbose_name=_('Finished At'), null=True, blank=True)
    successful = models.NullBooleanField(verbose_name=_('Successful'))

    class Meta:
        db_table = 'job'
        verbose_name = _('Job')
        verbose_name_plural = _('Jobs')
