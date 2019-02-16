# -*- coding: utf-8 -*-
""" Created by Safa Arıman on 2/16/19 """
from url_filter.filtersets import ModelFilterSet

from farm.models import Job

__author__ = 'safaariman'


class JobFilterSet(ModelFilterSet):

    class Meta:
        model = Job
