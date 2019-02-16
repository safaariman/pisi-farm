# -*- coding: utf-8 -*-
""" Created by Safa Arıman on 2/16/19 """
from rest_framework_json_api.serializers import ModelSerializer

from farm.models import Job

__author__ = 'safaariman'


class JobSerializer(ModelSerializer):

    class Meta:
        model = Job
        fields = '__all__'
