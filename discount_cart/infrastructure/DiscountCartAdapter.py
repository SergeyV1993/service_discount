from ..models import DiscountCart


class DiscountCartInfoAdapter:

    def adapt_discount_cart(self, discount_info: DiscountCart) -> DiscountCart:
        return discount_info

    def adapt_discount_cart_status(self, discount_info: DiscountCart, cart_number: int) -> None:
        discount_info.cart, discount_info.status = cart_number, False
        discount_info.save(update_fields=["cart", "status"])
