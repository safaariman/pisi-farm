# -*- coding: utf-8 -*-
""" Created by Safa Arıman on 2/16/19 """
from farm.celery import app
from farm.models import Job

__author__ = 'safaariman'


@app.task(bind=True)
def debug_task(task, *args, **kwargs):
    job = Job.objects.get(pk=kwargs.get('job'))
    job.task_id = task.request.id
    job.save()
    print('This is a test task.')
