# -*- coding: utf-8 -*-
""" Created by Safa Arıman on 2/15/19 """
from django.contrib import admin

from farm.models import Repository

__author__ = 'safaariman'


@admin.register(Repository)
class RepositoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'branch', 'image', 'directory', 'enabled')
    search_fields = ('name', 'url', 'branch', 'image', 'directory', 'enabled')
    list_filter = ('enabled', )
