# -*- coding: utf-8 -*-
""" Created by Safa Arıman on 3/6/19 """
from django_celery_results.models import TaskResult
from rest_framework_json_api.serializers import ModelSerializer

__author__ = 'safaariman'


class TaskResultSerializer(ModelSerializer):

    class Meta:
        model = TaskResult
        fields = '__all__'

