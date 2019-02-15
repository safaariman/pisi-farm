# -*- coding: utf-8 -*-
""" Created by Safa Arıman on 2/15/19 """
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from farm.admin.repository import RepositoryAdmin
from farm.admin.package import PackageAdmin
from farm.admin.job import JobAdmin

__author__ = 'safaariman'


admin.site.site_header = _('Pisi Farm Administration Console')
admin.site.site_title = _('Pisi Farm Administration Console')
