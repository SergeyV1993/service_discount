from discount_cart.domain.Dto.DiscountCartDto import DiscountCartDto
from discount_cart.models import DiscountCart


class DiscountCartFactory:

    def __init__(self):
        self.discount_cart_info = DiscountCartDto()

    def create_discount_cart(self, discount_cart: DiscountCart) -> DiscountCartDto:

        self.discount_cart_info.set_nominal(discount_cart.nominal)
        self.discount_cart_info.set_status(discount_cart.status)
        self.discount_cart_info.set_valid_date_end(discount_cart.valid_date_end)
        self.discount_cart_info.set_cart(discount_cart.cart)
        self.discount_cart_info.set_code(discount_cart.code)

        return self.discount_cart_info
