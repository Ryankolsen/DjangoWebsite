from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    #calls to create user profile - see signals.py
    def ready(self):
        import users.signals
