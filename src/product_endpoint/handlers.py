import json

from src.product.infrastructure.in_memory_product_repository import InMemoryProductRepository
from src.product.product import Product
from src.product.product_category import ProductCategory
from src.product.product_service import ProductService
from src.product.value_objects import ProductId

PRODUCT_ID = ProductId(str('64a49c5b-0d0a-4640-8a4b-3e64ddde0d4f'))

PRODUCT = Product(
    price=9.99,
    category=ProductCategory.VIDEO,
    name='Breaking Bad',
    id=PRODUCT_ID
)

product_repository = InMemoryProductRepository()
product_repository.add_product(product=PRODUCT)
product_service = ProductService(product_repository=product_repository)


def get_product_handler(event, context) -> dict:
    product_id = event['pathParameters']['product_id']
    product = product_service.find_product_by_id(product_id=product_id)

    return {
        "statusCode": 200,
        "body": json.dumps({
            'product_id': product.id,
            'name': product.name,
            'price': product.price,
            'category': product.category
        }),
    }


def add_product_handler(event, context) -> dict:
    payload = json.loads(event['body'])
    product_service.add_product(
        product_id=payload['product_id'],
        name=payload['name'],
        price=payload['price'],
        category=payload['category']
    )

    return {"statusCode": 201}
