from django.db import models
from account.models import UserAccount
from food.models import Food

class Cart(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.food.name)


# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from order.models import Order

@receiver(post_save, sender=Cart)
def create_order(sender, instance, created, **kwargs):
    if created:
        order = Order.objects.filter(user=instance.user, status='Pending').first()
        if not order:
            order = Order.objects.create(user=instance.user)
        order.cart = instance
        order.save()
