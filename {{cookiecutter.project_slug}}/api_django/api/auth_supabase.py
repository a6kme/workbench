import logging
import os

from apps.authentication.models import UserProfile
from django.contrib.auth.models import User
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from supabase import Client, create_client

logger = logging.getLogger(__name__)

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_ANON_KEY")
auth_supabase: Client = create_client(url, key)


class SupabaseAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return None

        token = auth_header.split(' ')[1]
        user = self.verify_token_with_supabase(token)

        if user is None:
            raise AuthenticationFailed('Invalid token')

        return (user, None)

    def verify_token_with_supabase(self, token):
        # Use Supabase's `auth` API to verify the token
        try:
            response = auth_supabase.auth.get_user(token)
            if response.user:
                # Return a Django-like user object
                return self.get_or_create_django_user_object(response.user)
            return None
        except Exception as e:
            logger.info(f"Error verifying token: {str(e)}")
            return None

    def get_or_create_django_user_object(self, supabase_user):
        supabase_user_id = supabase_user.id
        try:
            return User.objects.select_related('profile').get(profile__federated_user_id=supabase_user_id, email=supabase_user.email)
        except User.DoesNotExist:
            logger.info(
                f"User not found in Django DB. Creating a new user profile for {supabase_user.email}")
            return self.create_new_user(supabase_user)

    def create_new_user(self, supabase_user):
        user = User.objects.create(
            username=supabase_user.email,
            email=supabase_user.email,
            first_name=supabase_user.user_metadata.get('full_name', ''),
        )
        profile = UserProfile.objects.create(
            user=user,
            federated_user_id=supabase_user.id,
            avatar_url=supabase_user.user_metadata.get('avatar_url', '')
        )
        user.profile = profile
        return user
