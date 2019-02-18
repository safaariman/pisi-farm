# -*- coding: utf-8 -*-
""" Created by Safa Arıman on 2/18/19 """
from django.test import TestCase

from farm.models import Package

__author__ = 'safaariman'


class PackageTestCase(TestCase):

    def test_string_representation(self):
        package = Package(name='test_package_name', description='Test package description.')
        self.assertEqual(str(package), package.name)
