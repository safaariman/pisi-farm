# -*- coding: utf-8 -*-
""" Created by Safa Arıman on 2/15/19 """
from farm.base.model import Model
from django.utils.translation import ugettext_lazy as _
from django.db import models

__author__ = 'safaariman'


class Repository(Model):
    name = models.CharField(verbose_name=_('Repository Name'), max_length=100)
    url = models.CharField(verbose_name=_('Repository URL'), max_length=250)
    branch = models.CharField(verbose_name=_('Branch'), max_length=200)
    # image = models.CharField(verbose_name=_('Docker Image'), max_length=200)
    # directory = models.CharField(verbose_name=_('Directory'), max_length=500)
    enabled = models.BooleanField(verbose_name=_('Enabled'), default=True)

    class Meta:
        db_table = 'repository'
        verbose_name = _('Repository')
        verbose_name_plural = _('Repositories')

    def __str__(self):
        return self.name
