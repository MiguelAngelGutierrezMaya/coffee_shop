from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    name = forms.CharField(label="Product Name", max_length=200, required=True)
    description = forms.CharField(
        label="Product Description", max_length=300, required=True
    )
    price = forms.DecimalField(
        label="Product Price", max_digits=10, decimal_places=2, required=True
    )
    available = forms.BooleanField(label="Product Available", required=False)
    photo = forms.ImageField(label="Product Image", required=False)

    class Meta:
        model = Product
        fields = ["name", "description", "price", "available", "photo"]

    def save(self):
        product = Product(
            name=self.cleaned_data["name"],
            description=self.cleaned_data["description"],
            price=self.cleaned_data["price"],
            available=self.cleaned_data["available"],
            photo=self.cleaned_data["photo"],
        )

        product.save()
