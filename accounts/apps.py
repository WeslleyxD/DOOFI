import sys
from urllib.parse import urlparse

from django.apps import AppConfig


class CommonConfig(AppConfig):
    name = "accounts"
    verbose_name = "accounts"