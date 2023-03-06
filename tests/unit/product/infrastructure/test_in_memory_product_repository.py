# from constants import (
#     UPDATED_PRODUCT_WITH_OLD_ID,
#     PRODUCT_ID_BREAKING_BAD,
#     PRODUCT_VIDEO_BREAKING_BAD,
# )
from uuid import uuid4

from src.product.product import Product
from src.product.product_category import ProductCategory
from src.product.value_objects import ProductId

PRODUCT_ID = ProductId(str(uuid4()))

PRODUCT_VIDEO_BREAKING_BAD = Product(
    price=9.99,
    category=ProductCategory.VIDEO,
    name='Breaking Bad',
    id=PRODUCT_ID
)


class TestProductRepositoryShould:
    def test_return_product_by_id(self, product_repository) -> None:
        product_repository.add_product(PRODUCT_VIDEO_BREAKING_BAD)
        expected_product = product_repository.find_product_by_id(PRODUCT_ID)
        assert expected_product == PRODUCT_VIDEO_BREAKING_BAD

    def test_return_nothing_when_product_doesnt_exist(self, product_repository) -> None:
        expected_product = product_repository.find_product_by_id(ProductId(str(uuid4())))
        assert expected_product is None
