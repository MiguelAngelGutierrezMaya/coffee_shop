from django.contrib import admin
from .models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['name', 'price', 'available', 'created_at']
    list_filter = ['available', 'created_at']
    search_fields = ['name', 'description']
    list_editable = ['price', 'available']
    date_hierarchy = 'created_at'


admin.site.register(Product, ProductAdmin)
