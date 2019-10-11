# -*- coding: utf-8 -*-
""" Created by Safa Arıman on 2/16/19 """
from django.contrib import admin

from farm.models import Job

__author__ = 'safaariman'


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'event', 'state')
    search_fields = ('uuid', 'event', )
    list_filter = ('state', )
    readonly_fields = ('uuid', 'output', )
    actions = ('reset_jobs', )

    def get_queryset(self, request):
        return super(JobAdmin, self).get_queryset(request).select_related('event')

    def reset_jobs(self, request, queryset):
        queryset.update(state=Job.PENDING)
    reset_jobs.short_description = "Reset the jobs"
