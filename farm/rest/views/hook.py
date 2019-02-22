# -*- coding: utf-8 -*-
""" Created by Safa Arıman on 2/20/19 """
from rest_framework import viewsets

from farm.models import Hook
from farm.rest.filters.hook import HookFilterSet
from farm.rest.serializers.hook import HookSerializer

__author__ = 'safaariman'


class HookViewSet(viewsets.ModelViewSet):
    queryset = Hook.objects.all().order_by('-created_at')
    serializer_class = HookSerializer
    filter_class = HookFilterSet
