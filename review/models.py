from django.db import models
from django.contrib.auth.models import User
from account.models import UserAccount

STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]

class Review(models.Model):
    rating = models.CharField(choices = STAR_CHOICES, max_length = 10)
    name = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name