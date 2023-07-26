from django.dispatch import receiver
from django.db.models.signals import (
    post_save, pre_save
)

from .models import User, UserProfile


@receiver(pre_save, sender=User)
def check_user_profile(sender, instance, created=False, **kwargs):
    print("PRE SAVE CALLED : Details are : ")
    print(f"Sender   : {sender}")
    print(f"instance : {instance} ")
    print(f"created  : {created} ")
    print(f"kwargs   : {kwargs} ")


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    print("POST SAVE CALLED : Details are : ")
    print(f"Sender   : {sender}")
    print(f"instance : {instance} ")
    print(f"created  : {created} ")
    print(f"kwargs   : {kwargs} ")

    if created:
        user = UserProfile.objects.create(user=instance)
        print(f"Post save signal : {user.user.name.upper()} profile created")
