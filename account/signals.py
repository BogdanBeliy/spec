from django.db.models.signals import post_save
from django.dispatch import receiver

from account.models import UserModel, PersonalArea


# @receiver(post_save, sender=UserModel)
# def create_personal_area(sender, instance, **kwargs):
#     PersonalArea.objects.create(user=instance)