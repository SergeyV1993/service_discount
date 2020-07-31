from datetime import *
from typing import Any

from rest_framework.response import Response
from rest_framework import status

from .DiscountServieInterface import DiscountServiceInterface
from discount_cart.models import DiscountCart
from discount_cart.infrastructure.DiscountRepository import DiscountRepository
from ..domain.DiscountAmountServiceInterface import DiscountAmountInterface


class DiscountService(DiscountServiceInterface):

    def __init__(self):
        self.discount_cart = DiscountRepository()
        self.discount_cart_amount = DiscountAmountInterface()

    def response_client_service(self, code: str, cart_number: int, cart_amount: float) -> Response:
        if self.__get_discount_cart(code) is None:
            return Response({"message": "Code does not exist"}, status=status.HTTP_404_NOT_FOUND)

        discount_cart = self.__get_discount_cart(code)
        if discount_cart.status and discount_cart.valid_date_end > datetime.now(timezone.utc):
            self.__set_discount_info(discount_cart, cart_number)

            return Response(
                {
                    "amount_cart": self.__get_discount_cart_amount(cart_amount, discount_cart.nominal),
                    "cart": cart_number
                },
            )

        return Response({"message": "Expired"}, status=status.HTTP_403_FORBIDDEN)

    def __get_discount_cart(self, code: str) -> Any:
        return self.discount_cart.get_discount_cart(code)

    def __get_discount_cart_amount(self, cart_amount: float, discount_amount: float) -> float:
        return self.discount_cart_amount.calculate_discount_amount_cart(cart_amount, discount_amount)

    def __set_discount_info(self, discount_info: DiscountCart, cart_number: int) -> None:
        return self.discount_cart.set_discount_info(discount_info, cart_number)
