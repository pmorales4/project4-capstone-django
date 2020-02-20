from django.apps import AppConfig


class MusicusersConfig(AppConfig):
    name = 'musicusers'

# method for the signals code
    def ready(self):
        import users.signals