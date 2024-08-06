from django.db import models


class User(models.Model):
    discord_id = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=100)
    avatar = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f'{self.username}'
