from abc import abstractmethod
from typing import Optional, Protocol

from src.product.product import Product
from src.product.value_objects import ProductId


class ProductRepository(Protocol):
    @abstractmethod
    def find_product_by_id(self, product_id: ProductId) -> Optional[Product]:
        pass

    @abstractmethod
    def add_product(self, product: Product) -> None:
        pass
