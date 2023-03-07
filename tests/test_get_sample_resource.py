import pytest
from uuid import UUID


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "resource_id, expected_status, expected_name",
    [
        ("5e8e793e-b7b6-4ad0-ba78-94445ef2a286", 200, "name A"),
        ("cef4485f-fed7-48e3-99c6-47da4c04a894", 200, "name B"),
        (None, 400, None),
        ("76805766-c436-405f-beb2-735075124a6e", 204, None),
        ("c0a207d1-1734-4052-b127-4845eb9d40bb", 204, None),
    ]
)
async def test_create_sample_resource(
    test_client, mongo_client, resource_id: UUID,
    expected_status: int, expected_name: str
):
    req_params = {}
    if None is not resource_id:
        req_params["resource"] = resource_id

    resp = test_client.get(
        '/api/sample-resource-app/v1/sample-resource',
        params=req_params,
    )
    assert resp.status_code == expected_status

    if 200 == expected_status:
        assert 'name' in resp.json()
        assert expected_name == resp.json().get('name')
