from django.apps import AppConfig


class MainAppConfig(AppConfig):
    name = 'main_app'

    def ready(self):
        import users.signals
            # this is the django recommended way