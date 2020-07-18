from datetime import *
from typing import Any

from rest_framework.response import Response
from rest_framework import status
from discount_cart.models import DiscountCart

from discount_cart.infrastructure.DiscountRepository import DiscountRepository
from discount_cart.domain.Discount import Discount


class DiscountService:

    def __init__(self):
        self.discount_cart = DiscountRepository()
        self.discount_cart_amount = Discount()

    def get_discount(self, code: str) -> Any:
        return self.discount_cart.get_discount_cart(code)

    def get_discount_cart_amount(self, cart_amount: float, discount_amount: float) -> float:
        return self.discount_cart_amount.calculate_discount_amount_cart(cart_amount, discount_amount)

    def set_discount_info(self, discount_info: DiscountCart, cart_number: int) -> None:
        return self.discount_cart.set_discount_info(discount_info, cart_number)

    def response(self, code: str, cart_number: int, cart_amount: float) -> Response:
        if self.get_discount(code) is None:
            return Response({"message": "Code does not exist"}, status=status.HTTP_404_NOT_FOUND)

        discount_cart = self.get_discount(code)
        if discount_cart.status and discount_cart.valid_date_end > datetime.now(timezone.utc):
            self.set_discount_info(discount_cart, cart_number)

            return Response(
                {
                    "amount_cart": self.get_discount_cart_amount(cart_amount, discount_cart.nominal),
                    "cart": cart_number
                },
            )

        return Response({"message": "Expired"}, status=status.HTTP_403_FORBIDDEN)
