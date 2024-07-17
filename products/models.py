from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Product Name")
    description = models.TextField(max_length=300, verbose_name="Product Description")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Product Price"
    )
    available = models.BooleanField(default=True, verbose_name="Product Available")
    photo = models.ImageField(
        upload_to="logos", null=True, blank=True, verbose_name="Product Photo"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
