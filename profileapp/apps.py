from django.apps import AppConfig


class ProfileappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profileapp'

    def ready(self):  # method to import signals
        import profileapp.signals
