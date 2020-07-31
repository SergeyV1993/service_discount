from discount_cart.domain.DiscountAmountServiceInterface import DiscountAmountInterface


class DiscountAmount(DiscountAmountInterface):

    def calculate_discount_amount_cart(self, cart_amount: float, discount_amount: float) -> float:
        return round(cart_amount - discount_amount, 2)
