from django.apps import AppConfig


class KsyshevConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ksyshev'

    def ready(self):
        from . import signals
