from django.contrib import admin
from .models import Order, OrderProduct


# Register your models here.


class OrderProductInlineAdmin(admin.TabularInline):
    model = OrderProduct
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [OrderProductInlineAdmin]
    list_display = ["id", "user", "is_active", "order_date"]
    list_filter = ["is_active", "order_date"]
    search_fields = ["user__username", "user__email"]
    readonly_fields = ["order_date"]


class OrderProductAdmin(admin.ModelAdmin):
    model = OrderProduct
    list_display = ["id", "order", "product", "quantity"]
    list_filter = ["order", "product"]
    search_fields = ["order__user__username", "order__user__email", "product__name"]


admin.site.register(Order, OrderAdmin)
