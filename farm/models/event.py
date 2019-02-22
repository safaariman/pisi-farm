# -*- coding: utf-8 -*-
""" Created by Safa Arıman on 2/20/19 """
from django.db import models
from django.db.models import TextField
from django.utils.translation import ugettext_lazy as _

from farm.base.model import Model
from farm.models import Hook

__author__ = 'safaariman'


class Event(Model):
    """
    Event model to store data coming from supported external sources like GitHub, GitLab, Bitbucket etc.
    """
    payload = TextField(verbose_name=_('Payload'))
    meta = TextField(verbose_name=_('Meta'))
    hook = models.ForeignKey(Hook, null=True, on_delete=models.SET_NULL, verbose_name=_('Hook'))

    class Meta:
        db_table = 'event'
        verbose_name = _('Event')
        verbose_name_plural = _('Events')
