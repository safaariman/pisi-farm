# -*- coding: utf-8 -*-
""" Created by Safa Arıman on 2/15/19 """
from django.db import models
from django.utils.translation import ugettext_lazy as _

__author__ = 'safaariman'


class Model(models.Model):
    created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

    class Meta:
        abstract = True
