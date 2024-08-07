from django.urls import path
from .views import ProductFormView, ProductListView, ProductListAPIView

urlpatterns = [
    path("", ProductListView.as_view(), name="list_products"),
    path("api/", ProductListAPIView.as_view(), name="list_products_api"),
    path("add/", ProductFormView.as_view(), name="add_product"),
]
