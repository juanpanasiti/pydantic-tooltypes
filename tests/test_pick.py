import pytest
from pydantic import ValidationError

from pydantic_tooltypes import Pick

from .models import User

PICK_KEYS: list[str] = ['email']
PickUser = Pick[User, PICK_KEYS]


def test_pick_default_name():
    assert PickUser.__name__ == 'PickUser'


def test_pick_fields_are_required():
    with pytest.raises(ValidationError):
        PickUser()


def test_not_picked_fields_are_ommited():
    user = PickUser(email='')
    assert user.model_dump() == {'email': ''}
