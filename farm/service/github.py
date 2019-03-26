# -*- coding: utf-8 -*-
""" Created by Safa Arıman on 3/7/19 """

__author__ = 'safaariman'


class GithubIntegration(object):
    """
    Github Integration
    """

    def __init__(self, payload: dict):
        """
        Github Integration constructor.

        Args:
            payload (dict): Github webhook payload.
        """
        self.payload = payload
