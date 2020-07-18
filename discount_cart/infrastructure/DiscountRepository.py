from typing import Any
from discount_cart.models import DiscountCart


class DiscountRepository:

    def get_discount_cart(self, code: str) -> Any:
        if DiscountCart.objects.filter(code=code).exists():
            return DiscountCart.objects.get(code=code)

    def set_discount_info(self, discount_info: DiscountCart, cart_number: int):
        discount_info.cart, discount_info.status = cart_number, False
        discount_info.save(update_fields=["cart", "status"])
