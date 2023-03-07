import pytest
from uuid import UUID


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "resource_id, name, expected_status",
    [
        ("5e8e793e-b7b6-4ad0-ba78-94445ef2a286", 'John Doe', 200),
        ("cef4485f-fed7-48e3-99c6-47da4c04a894", 'Jane Doe', 200),
        ("cddd67bf-48c0-4e4c-95c6-cec9ec1981b6", 'John Doe', 422),
        ("c0a207d1-1734-4052-b127-4845eb9d40bb", 'John Doe', 422),
        ("5e8e793e-b7b6-4ad0-ba78-94445ef2a286", None, 400),
    ]
)
async def test_update_sample_resource(
    test_client, mongo_client, resource_id: UUID,
    name: str, expected_status: int
):
    req_json = {}
    if None is not name:
        req_json["name"] = name

    resp = test_client.put(
        f'/api/sample-resource-app/v1/sample-resource/{resource_id}',
        json=req_json
    )
    assert resp.status_code == expected_status

    if 200 == expected_status:
        resource_db = await mongo_client.get_sample_resource(resource_id)
        assert resource_db.get('name') == name
