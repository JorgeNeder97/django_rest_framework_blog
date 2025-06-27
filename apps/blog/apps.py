from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.blog' # Agregamos apps. porque creamos una carpeta llamada apps y queremos que python la lea
