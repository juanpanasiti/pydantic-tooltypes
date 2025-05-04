from typing import Generic, Literal, TypeVar, get_type_hints
from pydantic import BaseModel, create_model

T = TypeVar('T', bound=BaseModel)

class Omit(Generic[T]):
    """
    Creates a new Pydantic model by excluding specific fields from the provided model.

    Usage:
        class User(BaseModel):
            id: int
            email: str

        OmitUser = Omit[User, ['id']]

        # OmitUser has only the 'email' field

    This behaves like TypeScript's `Omit<Type, Keys>` utility.

    Args:
        T (BaseModel): The base Pydantic model.
        keys (list[str]): Field names to exclude.

    Returns:
        A dynamically generated Pydantic model with the specified keys omitted.
    """
    def __class_getitem__(cls, params: tuple[type[T], list[str]]) -> type[BaseModel]:
        base_model, keys = params
        name = f'Omit{base_model.__name__}'
        annotations = get_type_hints(base_model, include_extras=True)

        fields = {
            k: (annotation, ...)
            for k, annotation in annotations.items()
            if k not in keys
        }

        return create_model(name, __base__=BaseModel, **fields)
