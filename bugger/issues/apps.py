from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class IssuesConfig(AppConfig):
    name = "bugger.issues"
    verbose_name = _("Issues")

    def ready(self):
        try:
            import bugger.users.signals  # noqa F401
        except ImportError:
            pass
