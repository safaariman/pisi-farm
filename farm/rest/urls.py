# -*- coding: utf-8 -*-
""" Created by Safa Arıman on 2/16/19 """
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from farm.rest.views.hook import HookViewSet
from farm.rest.views.job import JobViewSet
from farm.rest.views.repository import RepositoryViewSet
from farm.rest.views.package import PackageViewSet

__author__ = 'safaariman'


router = DefaultRouter()
router.register('jobs', JobViewSet)
router.register('repositories', RepositoryViewSet)
router.register('packages', PackageViewSet)
router.register('hooks', HookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
