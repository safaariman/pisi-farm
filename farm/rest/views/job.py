# -*- coding: utf-8 -*-
""" Created by Safa Arıman on 2/16/19 """
from rest_framework_json_api.views import ModelViewSet

from farm.models import Job
from farm.rest.filters.job import JobFilterSet
from farm.rest.serializers.job import JobSerializer

__author__ = 'safaariman'


class JobViewSet(ModelViewSet):
    queryset = Job.objects.select_related('task', 'event').order_by('-created_at')
    serializer_class = JobSerializer
    filter_class = JobFilterSet
