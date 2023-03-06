from uuid import uuid4

import pytest

from src.product.product import Product
from src.product.product_category import ProductCategory
from src.product.errors import ProductNotFoundError
from src.product.value_objects import ProductId
from src.product.product_service import ProductService

PRODUCT_ID = ProductId(str('64a49c5b-0d0a-4640-8a4b-3e64ddde0d4f'))

PRODUCT_VIDEO_BREAKING_BAD = Product(
    price=9.99,
    category=ProductCategory.VIDEO,
    name='Breaking Bad',
    id=PRODUCT_ID
)


class TestProductServiceShould:
    def test_return_product_by_id(self, mocked_product_repository, product_service: ProductService) -> None:
        mocked_product_repository.find_product_by_id.return_value = PRODUCT_VIDEO_BREAKING_BAD
        product = product_service.find_product_by_id(product_id=PRODUCT_ID)
        assert isinstance(product, Product)
        assert product.id == PRODUCT_ID
        assert product.name == 'Breaking Bad'
        assert product.category == ProductCategory.VIDEO

    def test_raise_error_when_product_is_not_found(
            self, mocked_product_repository, product_service
    ) -> None:
        mocked_product_repository.find_product_by_id.return_value = None
        with pytest.raises(ProductNotFoundError):
            product_service.find_product_by_id(product_id=PRODUCT_ID)

    def test_add_product(self, mocked_product_repository, product_service):
        product_service.add_product(
            product_id=PRODUCT_ID,
            name='Software Architecture The Hard Parts',
            price=20.00,
            category='Book'
        )
        mocked_product_repository.add_product.assert_called_once()
