from django.apps import AppConfig
from django.db.models import BigAutoField


class OnlinecourseConfig(AppConfig):
    name = 'onlinecourse'

    DEFAULT_AUTO_FIELD = BigAutoField
