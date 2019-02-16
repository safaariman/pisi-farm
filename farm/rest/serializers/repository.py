# -*- coding: utf-8 -*-
""" Created by Safa Arıman on 2/16/19 """
from rest_framework_json_api.serializers import ModelSerializer

from farm.models import Repository

__author__ = 'safaariman'


class RepositorySerializer(ModelSerializer):

    class Meta:
        model = Repository
        fields = '__all__'
