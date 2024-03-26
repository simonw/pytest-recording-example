import httpx
import os
import pytest


@pytest.fixture(scope="module")
def vcr_config():
    return {"filter_headers": ["x-api-key"]}


@pytest.mark.vcr()
def test_httpx_example_com():
    url = "https://example.com/"
    with httpx.Client() as client:
        response = client.get(url)
        assert response.status_code == 200

        content = response.text
        assert "<title>Example Domain</title>" in content


@pytest.mark.vcr()
def test_httpx_anthropic_claude():
    url = "https://api.anthropic.com/v1/messages"
    headers = {
        "x-api-key": os.environ.get("ANTHROPIC_API_KEY") or "mock-api-key",
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
    }
    data = {
        "model": "claude-3-haiku-20240307",
        "max_tokens": 50,
        "messages": [{"role": "user", "content": "Haiku about a pelican"}],
    }

    with httpx.Client() as client:
        response = client.post(url, json=data, headers=headers)
        assert response.status_code == 200

        content = response.json()
        assert content["content"][0]["text"] == (
            "Here is a haiku about a pelican:\n\n"
            "Graceful, soaring bird\n"
            "Diving for its fishy prey\n"
            "Pelican's feast time"
        )
