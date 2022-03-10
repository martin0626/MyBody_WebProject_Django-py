from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from MyBody.catalog.helpers import add_user_to_default_group
from MyBody.users.helpers import send_email_message
from MyBody.users.models import Profile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, **kwargs):
    if created:
        profile = Profile(
            user=instance,
        )
        email = instance.email
        username = instance.username
        add_user_to_default_group(user=instance)
        send_email_message(email, username)
        profile.save()
