from datetime import *
from typing import Any

from rest_framework.response import Response
from rest_framework import status

from .DiscountServieInterface import DiscountServiceInterface

from ..domain.DiscountAmountService import DiscountAmount
from ..domain.Dto import DiscountCartDto
from ..infrastructure.DiscountRepository import DiscountRepository


class DiscountService(DiscountServiceInterface):

    def __init__(self):
        self.discount_cart = DiscountRepository()
        self.discount_cart_amount = DiscountAmount()

    def response_client_service(self, code: str, cart_number: int, cart_amount: float) -> Response:
        if self.__get_discount_cart(code) is None:
            return Response({"message": "Code does not exist"}, status=status.HTTP_404_NOT_FOUND)

        discount_cart = self.__get_discount_cart(code)
        if discount_cart.get_status() and discount_cart.get_valid_date_end() > datetime.now(timezone.utc):
            discount_cart.set_cart(cart_number)
            discount_cart.set_status(False)
            self.__save_discount_cart(discount_cart)

            return Response(
                {
                    "amount_cart": self.__get_discount_cart_amount(cart_amount, discount_cart.get_nominal()),
                    "cart": cart_number
                },
            )

        return Response({"message": "Expired"}, status=status.HTTP_403_FORBIDDEN)

    def __get_discount_cart(self, code: str) -> Any:
        return self.discount_cart.find_discount_cart_by_code(code)

    def __get_discount_cart_amount(self, cart_amount: float, discount_amount: float) -> float:
        return self.discount_cart_amount.calculate_discount_amount_cart(cart_amount, discount_amount)

    def __save_discount_cart(self, discount_info: DiscountCartDto) -> None:
        self.discount_cart.save_discount_cart(discount_info)
