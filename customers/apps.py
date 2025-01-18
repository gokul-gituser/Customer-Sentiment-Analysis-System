from django.apps import AppConfig

#configures the customers app
class CustomersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customers'
