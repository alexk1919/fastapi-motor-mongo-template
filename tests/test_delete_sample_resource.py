import pytest
from uuid import UUID


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "resource_id, expected_status",
    [
        ("5e8e793e-b7b6-4ad0-ba78-94445ef2a286", 200),
        ("cef4485f-fed7-48e3-99c6-47da4c04a894", 200),
        ("c0a207d1-1734-4052-b127-4845eb9d40bb", 422),
        (None, 405),
    ]
)
async def test_delete_sample_resource(
    test_client, mongo_client, resource_id: UUID, expected_status: int
):

    path = '/api/sample-resource-app/v1/sample-resource'
    if None is not resource_id:
        path = f'{path}/{resource_id}'

    resp = test_client.delete(
        path,
    )
    assert resp.status_code == expected_status

    if 200 == resp.status_code:
        resource_db = await mongo_client.get_sample_resource(resource_id)
        assert True is resource_db.get('deleted')
