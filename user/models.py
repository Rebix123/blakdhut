from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings 
import uuid

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    full_name = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    referral_code = models.CharField(max_length=50, unique=True, blank=True)
    referred_by = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='referrals')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.referral_code:
            self.referral_code = str(uuid.uuid4()).upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username}'s Profile"

class Coin(models.model):
    name = models.CharField(max_length=20)
    symbol = models.CharField(max_length=10)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name
