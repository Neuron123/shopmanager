from django.apps import AppConfig
from django.core.signals import request_started
from .tasks import log_request

