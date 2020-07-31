from discount_cart.models import DiscountCart


class DiscountCartGateway:

    def find_by_code(self, code: str) -> DiscountCart:
        if DiscountCart.objects.filter(code=code).exists():
            discount_cart = DiscountCart.objects.get(code=code)

            return discount_cart

    def save_discount_cart(self, status: bool, cart_number: int, code: str) -> None:
        discount_cart = DiscountCart.objects.get(code=code)

        discount_cart.cart = cart_number
        discount_cart.status = status

        discount_cart.save(update_fields=["cart", "status"])
