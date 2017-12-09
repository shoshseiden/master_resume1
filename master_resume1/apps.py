from importlib import import_module

from django.apps import AppConfig as BaseAppConfig


class AppConfig(BaseAppConfig):

    name = "master_resume1"

    def ready(self):
        import_module("master_resume1.receivers")
