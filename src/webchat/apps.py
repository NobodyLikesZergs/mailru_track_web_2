from __future__ import unicode_literals

from django.apps import AppConfig


class WebchatConfig(AppConfig):
    name = 'webchat'
    def ready(self):
        import signals
