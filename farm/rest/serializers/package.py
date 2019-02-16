# -*- coding: utf-8 -*-
""" Created by Safa Arıman on 2/16/19 """
from rest_framework_json_api.serializers import ModelSerializer

from farm.models import Package

__author__ = 'safaariman'


class PackageSerializer(ModelSerializer):

    class Meta:
        model = Package
        fields = '__all__'
