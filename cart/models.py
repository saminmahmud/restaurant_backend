from django.db import models
from account.models import UserAccount
from food.models import Food

class Cart(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.food.name)
