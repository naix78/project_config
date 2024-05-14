from django.urls import path
from .views import catalog, orders, product_detail, create_order


urlpatterns = [
    path('', catalog, name="catalog"), 
    path('orders/', orders, name="orders"),
    path('product_detail/<int:product_id>/', product_detail, name="product_detail"),
    path('create_order/<int:product_id>/', create_order, name="create_order")
]