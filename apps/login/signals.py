import datetime

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_login_failed
from django.dispatch import receiver
from django.utils import timezone
from apps.user.models import Profile


from apps.login.models import UserActivity


@receiver(post_save, sender=User)
def create_user_activity(sender, instance, created, **kwargs):
    if created:
        UserActivity.objects.create(user=instance)


@receiver(user_login_failed)
def increase_login_attempts(sender, credentials, request, **kwargs):
    username = credentials['username']
    user = User.objects.get(username=username)
    user_activity = user.activity
    if user_activity.login_attempts < 2:
        user_activity.login_attempts += 1
        user_activity.save()
    elif user_activity.login_attempts == 2:
        user_activity.login_attempts += 1
        user_activity.can_login_at = timezone.now() + datetime.timedelta(seconds=30)
        user_activity.save()



@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)