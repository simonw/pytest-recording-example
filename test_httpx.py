import httpx
import pytest


@pytest.mark.vcr()
def test_httpx_example_com():
    url = "https://example.com/"
    with httpx.Client() as client:
        response = client.get(url)
        assert response.status_code == 200

        content = response.text
        assert "<title>Example Domain</title>" in content
