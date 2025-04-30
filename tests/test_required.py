import pytest
from pydantic import ValidationError

from pydantic_tooltypes import Required

from .models import User
from .test_partial import PartialUser

REQUIRED_KEYS: list[str] = ['email']
RequiredUser = Required(PartialUser, keys=REQUIRED_KEYS)


def test_required_default_name():
    assert RequiredUser.__name__ == f'Required{PartialUser.__name__}'

def test_required_fields_are_required():
    user = RequiredUser(email='')
    assert user.model_dump(exclude_none=True) == {'email': ''}

    with pytest.raises(ValidationError):
        RequiredUser()

def test_number_of_fields():
    user = User(id=1, email='')
    required_user = RequiredUser(email='')
    assert len(user.model_dump()) == len(required_user.model_dump())