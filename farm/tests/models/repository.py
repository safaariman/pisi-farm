# -*- coding: utf-8 -*-
""" Created by Safa Arıman on 2/18/19 """
from django.test import TestCase

from farm.models import Package, Repository

__author__ = 'safaariman'


class RepositoryTestCase(TestCase):

    def test_string_representation(self):
        repository = Repository(name='test_repository_name')
        self.assertEqual(str(repository), repository.name)
