from django.db import models
from categories.models import Category
class Food(models.Model):
    categories = models.ManyToManyField(Category)

    image = models.ImageField(upload_to='food/media/')
    name = models.CharField(max_length=100)
    # description = models.TextField()
    price = models.IntegerField(default=0)
    def __str__(self):
        return self.name

