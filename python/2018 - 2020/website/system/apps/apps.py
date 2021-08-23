from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AppsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps'
    verbose_name = _('apps_config')

    def ready(self):
        import apps.signals
