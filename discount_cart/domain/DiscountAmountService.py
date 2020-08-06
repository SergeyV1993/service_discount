from discount_cart.domain.DiscountAmountServiceInterface import DiscountAmountInterface


class DiscountAmount(DiscountAmountInterface):

    def calculate_discount_amount_cart(self, cart_amount: float, discount_amount: float) -> float:
        total_discount_amount = round(float(cart_amount) - float(discount_amount), 2)

        if total_discount_amount < 0:
            return 0.0

        return total_discount_amount
