# -*- coding: utf-8 -*-
""" Created by Safa Arıman on 2/20/19 """
import json

from django.db.transaction import atomic
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from rest_framework.exceptions import NotFound
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from farm.models import Hook, Event

__author__ = 'safaariman'


class GitHubEventAPIView(APIView):

    permission_classes = (AllowAny, )
    parser_classes = (JSONParser, )

    @atomic
    def post(self, request, hash, format=None):
        try:
            hook = Hook.objects.get(source=Hook.GITHUB, url_hash=hash, is_active=True)
            hook.last_trigger = timezone.now()
            hook.save()

            payload = request.data
            meta = request.META

            headers = {header: value for header, value in meta.items() if header.startswith('HTTP')}
            event = Event(payload=json.dumps(payload), meta=json.dumps(headers), hook=hook)
            event.save()
        except Hook.DoesNotExist:
            raise NotFound(_('GitHub hook definition not found.'))

        return Response('OK')
