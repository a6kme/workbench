from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')

    # User ID provided by auth provider (supabase/ keycloak/ cognito etc.)
    federated_user_id = models.CharField(max_length=255, unique=True)
    avatar_url = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = 'user_profile'

    def __str__(self):
        return self.user.email
