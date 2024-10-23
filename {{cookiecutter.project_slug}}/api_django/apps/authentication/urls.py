from django.urls import path

from .views.celery_test import CeleryTestView
from .views.profile import ProfileView

urlpatterns = [
    path('user/profile/', ProfileView.as_view(), name='get-user-profile'),
    path('celery-test/', CeleryTestView.as_view(), name='celery-test'),
]
