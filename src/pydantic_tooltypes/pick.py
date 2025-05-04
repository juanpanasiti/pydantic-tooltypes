from typing import Any, Type, get_type_hints
from pydantic import BaseModel, create_model

class Pick:
    """
    A utility to create a new Pydantic model including only the specified fields.

    Example:
        PickUser = Pick[User, ['email']]

    This returns a new model with only the 'email' field from the User model.
    """

    def __class_getitem__(cls, params: tuple[Type[BaseModel], list[str]]) -> Type[BaseModel]:
        base_model, keys = params
        name = f'Pick{base_model.__name__}'
        annotations = get_type_hints(base_model, include_extras=True)

        fields = {
            k: (annotation, ...)
            for k, annotation in annotations.items()
            if k in keys
        }

        return create_model(name, __base__=BaseModel, **fields)
