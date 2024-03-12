from django.db import models
from django.contrib.auth.models import User

class UserAccount(models.Model):
    user = models.OneToOneField(User,related_name='account', on_delete=models.CASCADE)
    user_super = models.BooleanField(default=False)
    def __str__(self):
        return str(self.user.username)
    