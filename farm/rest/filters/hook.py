# -*- coding: utf-8 -*-
""" Created by Safa Arıman on 2/20/19 """
from url_filter.filtersets import ModelFilterSet

from farm.models import Hook

__author__ = 'safaariman'


class HookFilterSet(ModelFilterSet):

    class Meta:
        model = Hook
