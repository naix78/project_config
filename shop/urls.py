from django.urls import path
from .views import catalog, orders, product_detail


urlpatterns = [
    path('', catalog, name="catalog"), 
    path('orders/', orders, name="orders"),
    path('product_detail/<int:product_id>/', product_detail, name="product_detail")
]