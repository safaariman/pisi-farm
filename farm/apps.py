# -*- coding: utf-8 -*-
""" Created by Safa Arıman on 9/13/19 """
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

__author__ = 'safaariman'


class FarmAppConfig(AppConfig):
    label = 'farm'
    name = 'farm'
    verbose_name = _('Build Farm')
