from django.db import models
from account.models import UserAccount
from cart.models import Cart
from food.models import Food

STATUS = [
    ('Completed', 'Completed'),
    ('Pending', 'Pending'),
]

class Order(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    food = models.ForeignKey(Food , on_delete=models.CASCADE, null=True, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0)
    status = models.CharField(choices = STATUS, max_length = 10, default = "Pending")

    def __str__(self):
        return str(self.user.user.username)

