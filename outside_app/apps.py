from django.apps import AppConfig


class OutsideAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'outside_app'
