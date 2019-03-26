# -*- coding: utf-8 -*-
""" Created by Safa Arıman on 2/16/19 """
from rest_framework_json_api.serializers import ModelSerializer

from farm.models import Job
from farm.rest.serializers.task_result import TaskResultSerializer

__author__ = 'safaariman'


class JobSerializer(ModelSerializer):

    included_serializers = {
        'task': TaskResultSerializer,
    }

    class Meta:
        model = Job
        fields = '__all__'
