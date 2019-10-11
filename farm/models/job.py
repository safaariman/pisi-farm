# -*- coding: utf-8 -*-
""" Created by Safa Arıman on 2/16/19 """
import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _

from farm.base.model import Model
from farm.models import Event

__author__ = 'safaariman'


class Job(Model):
    PENDING, IN_PROGRESS, CANCELED, FAILED, COMPLETED = ('pending', 'in_progress', 'canceled', 'failed', 'completed')

    JOB_STATE_CHOICES = [
        (PENDING, 'Pending'),
        (IN_PROGRESS, 'In Progress'),
        (CANCELED, 'Canceled'),
        (FAILED, 'Failed'),
        (COMPLETED, 'Completed')
    ]

    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False, unique=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    state = models.CharField(max_length=50, choices=JOB_STATE_CHOICES, default=PENDING)
    output = models.TextField(null=True, blank=True)

    def update_state(self, new_state: str):
        self.state = new_state
        self.save()

    def append_output(self, output: str):
        if self.output:
            self.output += output
        else:
            self.output = output
        self.save()

    class Meta:
        db_table = 'job'
        verbose_name = _('Job')
        verbose_name_plural = _('Jobs')
