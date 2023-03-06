import requests


def test_api_gateway(api_gateway_url):
    """ Call the API Gateway endpoint and check the response """
    response = requests.get(api_gateway_url + '/ping')

    assert response.status_code == 200
    assert response.json() == {"ping": "pong"}
