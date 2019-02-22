# -*- coding: utf-8 -*-
""" Created by Safa Arıman on 2/22/19 """
from urllib.parse import urljoin

from django.conf import settings
from django.test import TestCase

from farm.models import Hook

__author__ = 'safaariman'


class HookTestCase(TestCase):

    def test_url_hash_generation(self):
        hook = Hook(source=Hook.GITHUB)
        hook.save()
        self.assertIsNotNone(
            hook.url_hash,
            'Url hash generation has failed.'
        )

    def test_secret_token_generation(self):
        hook = Hook(source=Hook.GITHUB)
        hook.save()
        self.assertIsNotNone(
            hook.secret,
            'Secret token generation has failed.'
        )

    def test_hook_url_generation(self):
        site_url = settings.SITE_URL
        hook = Hook(source=Hook.GITHUB, url_hash='hash_test')
        hook.save()
        self.assertEqual(
            hook.url,
            urljoin(site_url, '/hooks/{}/{}/'.format('github', 'hash_test')),
            'Hook URL generation has failed.'
        )

    def test_string_representation(self):
        hook = Hook(source=Hook.GITHUB)
        hook.save()
        self.assertEqual(
            str(hook),
            '{} - {}'.format(hook.get_source_display(), hook.url_hash),
            'String representation test has failed.'
        )
