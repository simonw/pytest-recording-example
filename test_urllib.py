import urllib.request
import pytest


@pytest.mark.vcr()
def test_urllib_example_com():
    url = "https://example.com/"
    response = urllib.request.urlopen(url)
    assert response.status == 200

    content = response.read().decode("utf-8")
    assert "<title>Example Domain</title>" in content
