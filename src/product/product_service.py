from typing import Optional

from src.product.product import Product
from src.product.errors import ProductNotFoundError
from src.product.product_category import ProductCategory
from src.product.value_objects import ProductId
from src.product.product_repository import ProductRepository


class ProductService:
    def __init__(
            self, product_repository: ProductRepository
    ):
        self._product_repository = product_repository

    def find_product_by_id(self, product_id: ProductId) -> Optional[Product]:
        product = self._product_repository.find_product_by_id(product_id=product_id)
        if product is None:
            raise ProductNotFoundError()
        return product

    def add_product(self, product_id: ProductId, name: str, price: float, category: str):
        product = Product(
            id=ProductId(product_id),
            name=name,
            price=price,
            category=ProductCategory(category)
        )
        self._product_repository.add_product(product)
