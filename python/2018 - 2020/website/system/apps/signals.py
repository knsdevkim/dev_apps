from django.db.models.signals import pre_save
from django.dispatch import receiver

import string
import random

from .models import WebContentModel, ApplicationFormModel, DepartmentModel, JobPositionModel

def generate_token(sender) -> str:

    def system_generate_token():
        MAX_CHARACTER = 100
        return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k = MAX_CHARACTER))
    
    token = system_generate_token()
    is_token_exists = sender.objects.filter(media_token = token).count()

    while is_token_exists > 0:
        token = system_generate_token()
        is_token_exists = sender.objects.filter(media_token = token).count()

    return token

@receiver(pre_save, sender = WebContentModel)
def generate_web_contents_token(sender, instance, **kwargs):
    instance.media_token = generate_token(sender)

@receiver(pre_save, sender = ApplicationFormModel)
def generate_application_form_media_token(sender, instance, **kwargs):
    instance.media_token = generate_token(sender)

@receiver(pre_save, sender = JobPositionModel)
def generate_application_form_media_token(sender, instance, **kwargs):
    instance.media_token = generate_token(sender)
