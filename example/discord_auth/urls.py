from django.urls import path, include

from .views import save_discord_user

urlpatterns = [
    path('', include('django_discord_oauth2.urls')),
    path('save-user/', save_discord_user, name='save_discord_user'),
]
