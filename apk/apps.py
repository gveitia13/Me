from django.apps import AppConfig


class ApkConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apk'
    verbose_name = 'Categorías | Ropas'

    def ready(self):
        import apk.signals
