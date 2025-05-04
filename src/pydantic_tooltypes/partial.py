from typing import Optional, TypeVar, Generic, get_type_hints
from pydantic import BaseModel, create_model

T = TypeVar('T', bound=BaseModel)


class Partial(Generic[T]):
    """
    Creates a new Pydantic model where all fields from the provided model are optional.

    Usage:
        class User(BaseModel):
            id: int
            email: str

        PartialUser = Partial[User]

        # Now PartialUser has all fields optional:
        user = PartialUser()  # valid, no fields required

    Args:
        T (BaseModel): The base Pydantic model to transform.

    Returns:
        A dynamically created subclass of BaseModel with all fields optional.
    """
    def __class_getitem__(cls, model: type[T]) -> type[BaseModel]:
        name = f'Partial{model.__name__}'
        annotations = get_type_hints(model, include_extras=True)

        fields = {
            field: (Optional[annotation], None)
            for field, annotation in annotations.items()
        }

        return create_model(name, __base__=BaseModel, **fields)
