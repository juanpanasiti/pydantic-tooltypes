import pytest

from pydantic_tooltypes import Partial

from .models import User

PartialUser = Partial[User]


def test_partial_fields_are_optional():
    user = PartialUser()
    assert user.model_dump(exclude_none=True) == {}


def test_partial_model_default_name():
    assert PartialUser.__name__ == 'PartialUser'


def test_no_error_in_model_creation():
    try:
        user = PartialUser()
    except Exception:
        pytest.fail("Creating PartialUser raised an unexpected exception")


def test_number_of_fields_are_equals():
    user = User(id=1, email='')
    partial_user = PartialUser()
    assert len(user.model_dump()) == len(partial_user.model_dump())


def test_fields_can_be_setted():
    TEST_MAIL = 'test@mail.com'
    user = PartialUser(id=1, email=TEST_MAIL)

    assert user.id == 1
    assert user.email == TEST_MAIL


def test_fields_are_optional_by_default():
    user = PartialUser()
    assert user.id is None
    assert user.email is None
