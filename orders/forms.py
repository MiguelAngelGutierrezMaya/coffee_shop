from django.forms import ModelForm
from .models import OrderProduct


class OrderProductForm(ModelForm):
    class Meta:
        model = OrderProduct
        fields = [
            "product",
            # 'quantity'
        ]
        labels = {
            "product": "Product",
            # 'quantity': 'Quantity'
        }
        # widgets = {
        #     'product': forms.Select(attrs={'class': 'form-control'}),
        #     'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        # }
