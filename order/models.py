from django.db import models
from account.models import UserAccount
from cart.models import Cart

STATUS = [
    ('Completed', 'Completed'),
    ('Pending', 'Pending'),
]

class Order(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null= True, blank=True)
    status = models.CharField(choices = STATUS, max_length = 10, default = "Pending")

    def __str__(self):
        return str(self.user.user.username)

