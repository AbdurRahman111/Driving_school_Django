
from django.urls import path
from . import views
from .views import PaymentView


urlpatterns = [
    path('my_orders', views.my_orders, name='my_orders'),
    path('my_order_details/<int:pk>', views.my_order_details, name='my_order_details'),
    path('customer_canceled_order', views.customer_canceled_order, name='customer_canceled_order'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('payment', PaymentView.as_view(), name='payment'),

]
