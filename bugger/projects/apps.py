from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "bugger.projects"
    verbose_name = _("Projects")

    def ready(self):
        try:
            import bugger.projects.signals  # noqa F401
        except ImportError:
            pass
