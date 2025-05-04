import pytest
from pydantic import ValidationError

from pydantic_tooltypes import Omit

from .models import User

OMIT_KEYS: list[str] = ['id']
OmitUser = Omit[User, OMIT_KEYS]


def test_omit_default_name():
    assert OmitUser.__name__ == 'OmitUser'


def test_omit_fields_are_required():
    user = OmitUser(email='')
    assert user.model_dump(exclude_none=True) == {'email': ''}

    with pytest.raises(ValidationError):
        OmitUser()


def test_number_of_fields():
    user = User(id=1, email='')
    omit_user = OmitUser(email='')
    assert len(user.model_dump()) == (len(omit_user.model_dump()) + len(OMIT_KEYS))
