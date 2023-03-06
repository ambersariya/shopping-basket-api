from typing import Dict, Optional

from src.product.product import Product
from src.product.value_objects import ProductId
from src.product.product_repository import ProductRepository


class InMemoryProductRepository(ProductRepository):
    def __init__(self) -> None:
        self._products: Dict[ProductId, Product] = {}

    def find_product_by_id(self, product_id: ProductId) -> Optional[Product]:
        if product_id in self._products:
            return self._products[product_id]
        return None

    def add_product(self, product: Product) -> None:
        self._products[product.id] = product
