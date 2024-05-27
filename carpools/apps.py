from django.apps import AppConfig
# from django.conf import settings


class CarpoolsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'carpools'

    # def ready(self):
    #     if settings.SCHEDULER_DEFAULT:
    #         from . import operator
    #         operator.start()