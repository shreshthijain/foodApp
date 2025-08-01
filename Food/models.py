from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=100)
    item_description = models.CharField(max_length=500)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    item_image = models.ImageField(upload_to='item_images/', blank=True, null=True)
    item_category = models.CharField(max_length=50)
    # item_available = models.BooleanField(default=True)

    def __str__(self):
        return self.item_name