# -*- coding: utf-8 -*-
""" Created by Safa Arıman on 8/4/19 """
import json

from django.db.transaction import atomic
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from rest_framework.exceptions import NotFound
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from farm.models import Hook, Event, Job
from farm.tasks import debug_task

__author__ = 'safaariman'


class EventAPIView(APIView):

    permission_classes = (AllowAny, )
    parser_classes = (JSONParser, )

    @atomic
    def post(self, request, hash, format=None):
        try:
            hook = Hook.objects.get(url_hash=hash, is_active=True)
            hook.last_trigger = timezone.now()
            hook.save()

            payload = request.data
            meta = request.META

            headers = {header: value for header, value in meta.items() if header.startswith('HTTP')}
            event = Event(payload=json.dumps(payload), meta=json.dumps(headers), hook=hook)
            event.save()

            job = Job.objects.create(event=event)

            debug_task.apply_async(job=job.pk)
        except Hook.DoesNotExist:
            raise NotFound(_('Hook definition not found.'))

        return Response('OK')
