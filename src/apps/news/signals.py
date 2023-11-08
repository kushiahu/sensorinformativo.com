# Django 
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os

# Models
from apps.news.models import News


@receiver(pre_delete, sender=News)
def delete_news_cover(sender, instance, **kwargs):
    # Elimina el archivo de imagen relacionado cuando se elimina la instancia de News
    print('>> instance')
    print(instance)
    if instance.cover:
    	instance.cover.delete(save=True)
        # image_path = instance.cover.path
        # if os.path.isfile(image_path):
        #     os.remove(image_path)
