import abc

from rest_framework.response import Response


class DiscountServiceInterface(abc.ABC):

    @abc.abstractmethod
    def response_client_service(self, code: str, cart_number: int, cart_amount: float) -> Response:
        pass
