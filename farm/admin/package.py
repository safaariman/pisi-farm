# -*- coding: utf-8 -*-
""" Created by Safa Arıman on 2/15/19 """
from django.contrib import admin

from farm.models import Package

__author__ = 'safaariman'


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
