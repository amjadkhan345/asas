from django.apps import AppConfig


class AbookConfig(AppConfig):
    name = 'abook'

def ready(self):
    import abook.signals
