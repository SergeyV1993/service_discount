from .DiscountCartFactory import DiscountCartFactory
from .Gateway.DiscountCartGateway import DiscountCartGateway

from ..domain.DiscountRepositoryInterface import DiscountRepositoryInterface
from ..domain.Dto import DiscountCartDto


class DiscountRepository(DiscountRepositoryInterface):

    def __init__(self):
        self.gateway = DiscountCartGateway()
        self.discount_cart_factory = DiscountCartFactory()

    def find_discount_cart_by_code(self, code: str) -> DiscountCartDto or None:
        discount_cart = self.gateway.find_by_code(code)

        if discount_cart is None:
            return None

        return self.discount_cart_factory.create_discount_cart(discount_cart)

    def save_discount_cart(self, discount_info: DiscountCartDto) -> None:
        self.gateway.save_discount_cart(
            discount_info.get_status(),
            discount_info.get_cart(),
            discount_info.get_code()
        )
