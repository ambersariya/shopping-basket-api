import json
from uuid import uuid4

import pytest

from src.product.product import Product
from src.product.product_category import ProductCategory
from src.product.value_objects import ProductId
from src.product_endpoint.handlers import add_product_handler, get_product_handler

PRODUCT_ID = ProductId(str('64a49c5b-0d0a-4640-8a4b-3e64ddde0d4f'))

PRODUCT = Product(
    price=9.99,
    category=ProductCategory.VIDEO,
    name='Breaking Bad',
    id=PRODUCT_ID
)


@pytest.fixture()
def apigw_event():
    """ Generates API GW Event"""
    return {
        "body": '',
        "resource": "/products/{product_id+}",
        "requestContext": {
            "resourceId": "123456",
            "apiId": "1234567890",
            "resourcePath": "/products/64a49c5b-0d0a-4640-8a4b-3e64ddde0d4f",
            "httpMethod": "GET",
            "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
            "accountId": "123456789012",
            "identity": {
                "apiKey": "",
                "userArn": "",
                "cognitoAuthenticationType": "",
                "caller": "",
                "userAgent": "Custom User Agent String",
                "user": "",
                "cognitoIdentityPoolId": "",
                "cognitoIdentityId": "",
                "cognitoAuthenticationProvider": "",
                "sourceIp": "127.0.0.1",
                "accountId": "",
            },
            "stage": "prod",
        },
        "queryStringParameters": {},
        "headers": {
            "Via": "1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)",
            "Accept-Language": "en-US,en;q=0.8",
            "CloudFront-Is-Desktop-Viewer": "true",
            "CloudFront-Is-SmartTV-Viewer": "false",
            "CloudFront-Is-Mobile-Viewer": "false",
            "X-Forwarded-For": "127.0.0.1, 127.0.0.2",
            "CloudFront-Viewer-Country": "US",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Upgrade-Insecure-Requests": "1",
            "X-Forwarded-Port": "443",
            "Host": "1234567890.execute-api.us-east-1.amazonaws.com",
            "X-Forwarded-Proto": "https",
            "X-Amz-Cf-Id": "aaaaaaaaaae3VYQb9jd-nvCd-de396Uhbp027Y2JvkCPNLmGJHqlaA==",
            "CloudFront-Is-Tablet-Viewer": "false",
            "Cache-Control": "max-age=0",
            "User-Agent": "Custom User Agent String",
            "CloudFront-Forwarded-Proto": "https",
            "Accept-Encoding": "gzip, deflate, sdch",
        },
        "pathParameters": {"proxy": "/products", "product_id": PRODUCT_ID},
        "httpMethod": "GET",
        "stageVariables": {"baz": "qux"},
        "path": "/products",
    }


def test_lambda_handler_should_product_details(apigw_event):
    ret = get_product_handler(apigw_event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert "product_id" in ret["body"]
    assert data["product_id"] == PRODUCT_ID
    assert data["name"] == 'Breaking Bad'
    assert data["price"] == 9.99
    assert data["category"] == 'Video'


def test_should_add_a_product_to_inventory(apigw_event):
    apigw_event['body'] = json.dumps({
        'product_id': '7407cbd7-55ad-4be8-b77f-0bb16bf0c345',
        'name': 'Software Architecture The Hard Parts',
        'price': 20.00,
        'category': 'Book'
    })
    apigw_event['pathParameters']['product_id'] = '7407cbd7-55ad-4be8-b77f-0bb16bf0c345'
    ret = add_product_handler(apigw_event, "")

    assert ret["statusCode"] == 201
    assert 'body' not in ret