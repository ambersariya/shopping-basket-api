from dataclasses import dataclass

from src.product.product_category import ProductCategory
from src.product.value_objects import ProductId


@dataclass(init=True, frozen=True)
class Product:
    id: ProductId
    name: str
    price: float
    category: ProductCategory
