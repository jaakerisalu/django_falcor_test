from django.apps import AppConfig
from django.core import checks

from tg_utils.checks import check_production_settings, check_sentry_config


class Django_falcor_testConfig(AppConfig):
    name = 'django_falcor_test'
    verbose_name = "Falcor Test"

    def ready(self):
        # Import and register the system checks
        checks.register(check_production_settings)
        checks.register(check_sentry_config)
