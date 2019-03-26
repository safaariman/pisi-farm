# -*- coding: utf-8 -*-
""" Created by Safa Arıman on 2/16/19 """
from django.contrib import admin

from farm.models import Job

__author__ = 'safaariman'


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    #list_display = ('started_at', 'finished_at', 'successful', )
    list_display = ('task', 'event', )
    #search_fields = ('started_at', 'finished_at', 'successful', )
    search_fields = ('task', 'event', )

    def get_queryset(self, request):
        return super(JobAdmin, self).get_queryset(request).select_related('task', 'event')
