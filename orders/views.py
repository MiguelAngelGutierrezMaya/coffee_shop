from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Order, OrderProduct
from .forms import OrderProductForm


# Create your views here.
class MyOrderView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "orders/my_order.html"
    context_object_name = "order"

    # pk_url_kwarg = 'order_id'
    # extra_context = {'title': 'My Orders'}

    def get_object(self, queryset=None):
        ### Get the active order for the current authenticated user
        return Order.objects.filter(user=self.request.user, is_active=True).first()


class CreateOrderProductView(LoginRequiredMixin, CreateView):
    model = OrderProduct
    template_name = "orders/create_order_product.html"
    form_class = OrderProductForm
    success_url = reverse_lazy("my_order")

    def form_valid(self, form):
        ### Get the active order for the current authenticated user or create a new one
        order, _ = Order.objects.get_or_create(user=self.request.user, is_active=True)
        form.instance.order = order
        form.instance.quantity = 1
        form.save()
        return super().form_valid(form)
