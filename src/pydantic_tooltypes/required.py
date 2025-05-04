from typing import Any, Type, get_type_hints
from pydantic import BaseModel, create_model

class Required:
    """
    A utility to make specific fields required in a (possibly partially optional) Pydantic model.

    Example:
        RequiredUser = Required[PartialUser, ['email']]

    This returns a model where 'email' is required again, even if the base model made it optional.
    """

    def __class_getitem__(cls, params: tuple[Type[BaseModel], list[str]]) -> Type[BaseModel]:
        base_model, keys = params
        name = f'Required{base_model.__name__}'
        annotations = get_type_hints(base_model, include_extras=True)

        fields = {
            k: (annotation, ...) if k in keys else (annotation, None)
            for k, annotation in annotations.items()
        }

        return create_model(name, __base__=BaseModel, **fields)
