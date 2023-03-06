import requests


def test_should_return_breaking_bad_video(api_gateway_url):
    """ Call the API Gateway endpoint and check the response """
    response = requests.get(api_gateway_url + '/products/64a49c5b-0d0a-4640-8a4b-3e64ddde0d4f')

    assert response.status_code == 200
    assert response.json() == {
        'category': 'Video',
        'name': 'Breaking Bad',
        'price': 9.99,
        'product_id': '64a49c5b-0d0a-4640-8a4b-3e64ddde0d4f'
    }


def test_should_add_book(api_gateway_url):
    """ Call the API Gateway endpoint and check the response """
    endpoint = api_gateway_url + '/products/7407cbd7-55ad-4be8-b77f-0bb16bf0c345'
    book = {
        "product_id": "7407cbd7-55ad-4be8-b77f-0bb16bf0c345",
        "name": "Software Architecture The Hard Parts",
        "price": 20.00,
        "category": "Book"
    }
    response = requests.post(endpoint, json=book)
    assert response.status_code == 201

    response = requests.get(endpoint, json=book)
    assert 'product_id' not in response.json()
