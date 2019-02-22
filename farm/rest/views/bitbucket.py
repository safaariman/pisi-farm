# -*- coding: utf-8 -*-
""" Created by Safa Arıman on 2/20/19 """
from django.db.transaction import atomic
from django.utils.translation import ugettext_lazy as _
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

__author__ = 'safaariman'


class BitbucketEventAPIView(APIView):

    permission_classes = (AllowAny, )
    parser_classes = (JSONParser, )

    @atomic
    def post(self, request, hash, format=None):
        # TODO: Implement Bitbucket hooks.
        return Response(_('Bitbucket hooks are not supported.'), status=501)
