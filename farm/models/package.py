# -*- coding: utf-8 -*-
""" Created by Safa Arıman on 2/15/19 """
from django.db import models
from django.utils.translation import ugettext_lazy as _
from farm.base.model import Model

__author__ = 'safaariman'


class Package(Model):
    name = models.CharField(verbose_name=_('Package Name'), max_length=100)
    description = models.TextField(verbose_name=_('Package Description'))

    class Meta:
        db_table = 'package'
        verbose_name = _('Package')
        verbose_name_plural = _('Packages')

    def __str__(self):
        return self.name
