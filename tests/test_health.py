import pytest


@pytest.mark.asyncio
async def test_health(test_client):
    resp = test_client.get('/health')
    assert 200 == resp.status_code
