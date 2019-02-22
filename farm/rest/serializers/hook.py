# -*- coding: utf-8 -*-
""" Created by Safa Arıman on 2/20/19 """
from rest_framework_json_api import serializers

from farm.models import Hook

__author__ = 'safaariman'


class HookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hook
        fields = ('created_at', 'updated_at', 'source', 'url', 'url_hash', 'secret', 'last_trigger', 'is_active', )
        read_only_fields = ('url_hash', 'secret', 'last_trigger', )
