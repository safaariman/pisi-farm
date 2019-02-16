# -*- coding: utf-8 -*-
""" Created by Safa Arıman on 2/16/19 """
from url_filter.filtersets import ModelFilterSet

from farm.models import Package

__author__ = 'safaariman'


class PackageFilterSet(ModelFilterSet):

    class Meta:
        model = Package
