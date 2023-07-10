from api.questions_api import api
from http import HTTPStatus
from utils.assertions import Assert


def test_list_users():
    res = api.list_users()

    assert res.status_code == HTTPStatus.OK
    # Assert.validate_schema(res.json())


def test_single_user_not_found():
    res = api.single_user_not_found()

    assert res.status_code == HTTPStatus.NOT_FOUND
    # Assert.validate_schema(res.json())


def test_single_user():
    res = api.single_user()

    assert res.status_code == HTTPStatus.OK
    # Assert.validate_schema(res.json())
    assert res.json()['data']['first_name'] == 'Janet'
    assert res.json() == {
        "data": {
            "id": 2,
            "email": "janet.weaver@reqres.in",
            "first_name": "Janet",
            "last_name": "Weaver",
            "avatar": "https://reqres.in/img/faces/2-image.jpg"
        },
        "support": {
            "url": "https://reqres.in/#support-heading",
            "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
        }
    }


def test_create_user():
    res = api.create('Pupa', 'Testirovshchik')

    assert res.status_code == HTTPStatus.CREATED
    # Assert.validate_schema(res.json())
    assert res.json()['name'] == 'Pupa' and res.json()['job'] == 'Testirovshchik'
    res_2 = api.delete_user(res.json()['id'])
    assert res_2.status_code == HTTPStatus.NO_CONTENT

