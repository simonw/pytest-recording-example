import httpx
import pytest


@pytest.mark.asyncio
@pytest.mark.vcr()
async def test_httpx_async_example_com():
    url = "https://example.com/"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        assert response.status_code == 200

        content = response.text
        assert "<title>Example Domain</title>" in content
