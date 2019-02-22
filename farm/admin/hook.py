# -*- coding: utf-8 -*-
""" Created by Safa Arıman on 2/19/19 """
from django.contrib import admin

from farm.models import Hook

__author__ = 'safaariman'


@admin.register(Hook)
class HookAdmin(admin.ModelAdmin):
    list_display = ('source', 'url', 'last_trigger', 'is_active', )
    search_fields = ('source', 'url', 'last_trigger', 'is_active', )
    readonly_fields = ('url', 'url_hash', 'secret', 'last_trigger', )
