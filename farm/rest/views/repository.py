# -*- coding: utf-8 -*-
""" Created by Safa Arıman on 2/16/19 """
from rest_framework_json_api.views import ModelViewSet

from farm.models import Repository
from farm.rest.filters.repository import RepositoryFilterSet
from farm.rest.serializers.repository import RepositorySerializer

__author__ = 'safaariman'


class RepositoryViewSet(ModelViewSet):
    queryset = Repository.objects.all().order_by('-created_at')
    serializer_class = RepositorySerializer
    filter_class = RepositoryFilterSet
