import requests
import pytest


@pytest.mark.vcr()
def test_requests_example_com():
    url = "https://example.com/"
    response = requests.get(url)
    assert response.status_code == 200

    content = response.text
    assert "<title>Example Domain</title>" in content
