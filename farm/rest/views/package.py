# -*- coding: utf-8 -*-
""" Created by Safa Arıman on 2/16/19 """
from rest_framework_json_api.views import ModelViewSet

from farm.models import Package
from farm.rest.filters.package import PackageFilterSet
from farm.rest.serializers.package import PackageSerializer

__author__ = 'safaariman'


class PackageViewSet(ModelViewSet):
    queryset = Package.objects.all().order_by('-created_at')
    serializer_class = PackageSerializer
    filter_class = PackageFilterSet
