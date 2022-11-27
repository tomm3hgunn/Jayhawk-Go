from django.apps import AppConfig


class OddsandeventsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "oddsAndEvents"

    def ready(self):
        import oddsAndEvents.signals
