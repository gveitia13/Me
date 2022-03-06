from django.apps import AppConfig


class ApkConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.apk'
    verbose_name = 'Categorías | Ropas | Gastos'

    def ready(self):
        import apps.apk.signals
