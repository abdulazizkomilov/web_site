from django.urls import path
from .views import item_list, CheckoutPegeView, ProductPageView

app_name = 'core'

urlpatterns = [
    path('', item_list, name='home-page'),
    path('checkout/', CheckoutPegeView.as_view(), name='checkout-page'),
    path('products/', ProductPageView.as_view(), name='product-page'),
]