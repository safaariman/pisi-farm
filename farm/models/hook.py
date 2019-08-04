# -*- coding: utf-8 -*-
""" Created by Safa Arıman on 2/19/19 """
from urllib.parse import urljoin

from django.conf import settings
from django.db import models
from django.utils.crypto import get_random_string
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

from farm.base.model import Model

__author__ = 'safaariman'


class Hook(Model):
    """
    Hook model to store hook definitions to receive events from supported external sources.
    """
    GITHUB = 'GITHUB'
    GITLAB = 'GITLAB'
    BITBUCKET = 'BITBUCKET'

    SOURCES = (
        (GITHUB, 'GitHub'),
        (GITLAB, 'GitLab'),
        (BITBUCKET, 'Bitbucket'),
    )

    source = models.CharField(
        verbose_name=_('Source'), choices=SOURCES, max_length=50,
        help_text=_('The source that this web hook will be used. '
                    'There are 3 supported sources. GitHub, GitLab and Bitbucket.')
    )
    url_hash = models.CharField(
        verbose_name=_('URL Hash'), unique=True, max_length=256,
        help_text=_('Random generated hash to use in web hook url.')
    )
    secret = models.CharField(
        verbose_name=_('Secret'), max_length=256,
        help_text=_('Random generated secret hash to identify the sender to increase the security.')
    )
    last_trigger = models.DateTimeField(
        verbose_name=_('Last Trigger'), null=True, blank=True,
        help_text=_('The date that the hook recently triggered.')
    )
    is_active = models.BooleanField(
        verbose_name=_('Active'), default=True, help_text=_('Enable or disable the web hook.')
    )

    @cached_property
    def url(self):
        """
        Generates web hook url.

        Returns:
            Url as string.
        """
        return urljoin(settings.SITE_URL, '/hook/{}/'.format(self.url_hash)) if self.url_hash else ''

    def save(self, *args, **kwargs):
        if not self.url_hash:
            self.url_hash = get_random_string(32)
        if not self.secret:
            self.secret = get_random_string(32)

        super(Hook, self).save(*args, **kwargs)

    def __str__(self):
        return '%s - %s' % (self.get_source_display(), self.url_hash)

    class Meta:
        db_table = 'hook'
        verbose_name = _('Hook')
        verbose_name_plural = _('Hooks')
