from django.apps import AppConfig
from .options import ExperimentOptions

class DecisionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'decisions'
    options = ExperimentOptions()