import abc


class DiscountAmountInterface(abc.ABC):

    @abc.abstractmethod
    def calculate_discount_amount_cart(self, cart_amount: float, discount_amount: float) -> float:
        pass
