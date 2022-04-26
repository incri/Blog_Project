from django.db import models
from django.contrib.auth.models import User


class UserActivity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='activity')
    login_attempts = models.PositiveSmallIntegerField(default=0)
    can_login_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'User Activities'

    def __str__(self) -> str:
        return f'activity for {self.user}'
