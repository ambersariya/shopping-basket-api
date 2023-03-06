import pytest

from src.product.infrastructure.in_memory_product_repository import InMemoryProductRepository
from src.product.product_repository import ProductRepository
from src.product.product_service import ProductService


@pytest.fixture()
def mocked_product_repository(mocker):
    return mocker.Mock(ProductRepository)


@pytest.fixture()
def product_repository():
    return InMemoryProductRepository()


@pytest.fixture()
def product_service(mocked_product_repository):
    return ProductService(product_repository=mocked_product_repository)
