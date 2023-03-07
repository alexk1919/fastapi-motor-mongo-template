import pytest


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "name, expected_status",
    [
        ('John Doe', 201),
        (None, 400),
    ]
)
async def test_create_sample_resource(
    test_client, mongo_client, name: str, expected_status: int
):
    req_json = {}
    if None is not name:
        req_json["name"] = name

    resp = test_client.post(
        '/api/sample-resource-app/v1/sample-resource',
        json=req_json
    )
    assert resp.status_code == expected_status

    if 201 == expected_status:
        assert 'id' in resp.json()
        resource_id = resp.json().get('id')
        resource_db = await mongo_client.get_sample_resource(resource_id)
        assert resource_db.get('name') == name
        assert False is resource_db.get('deleted')
