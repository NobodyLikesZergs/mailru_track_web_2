from __future__ import unicode_literals

from django.apps import AppConfig


class WeblikeConfig(AppConfig):
    name = 'weblike'
    def ready(self):
        import signals
