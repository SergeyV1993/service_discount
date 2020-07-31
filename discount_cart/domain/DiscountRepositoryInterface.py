import abc

from discount_cart.domain.Dto import DiscountCartDto


class DiscountRepositoryInterface(abc.ABC):

    @abc.abstractmethod
    def find_discount_cart_by_code(self, code: str) -> DiscountCartDto or None:
        pass

    @abc.abstractmethod
    def save_discount_cart(self, discount_info: DiscountCartDto) -> None:
        pass
