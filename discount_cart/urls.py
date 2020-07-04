from django.urls import path
from discount_cart.views import Discounts

urlpatterns = [
    path('', Discounts.as_view()),
]
