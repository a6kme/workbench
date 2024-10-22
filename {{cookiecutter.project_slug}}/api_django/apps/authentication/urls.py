from apps.authentication.views import ProfileView
from django.urls import path

urlpatterns = [
    path('user/profile/', ProfileView.as_view(), name='get-user-profile'),
]
