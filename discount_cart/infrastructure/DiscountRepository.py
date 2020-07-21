from discount_cart.models import DiscountCart
from .DiscountCartAdapter import DiscountCartInfoAdapter


class DiscountRepository:

    def __init__(self):
        self.discount_cart_adapter = DiscountCartInfoAdapter()

    def get_discount_cart(self, code: str) -> DiscountCart:
        if DiscountCart.objects.filter(code=code).exists():
            discount_cart = DiscountCart.objects.get(code=code)

            return self.discount_cart_adapter.adapt_discount_cart(discount_cart)

    def set_discount_info(self, discount_info: DiscountCart, cart_number: int) -> None:
        self.discount_cart_adapter.adapt_discount_cart_status(
            self.discount_cart_adapter.adapt_discount_cart(discount_info),
            cart_number
        )
