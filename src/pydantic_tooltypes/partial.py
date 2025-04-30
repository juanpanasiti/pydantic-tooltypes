from typing import Optional, get_type_hints
from pydantic import BaseModel, create_model

def Partial(base_model: type[BaseModel], name: str | None = None) -> type[BaseModel]:
    """
    Creates a new Pydantic model where all fields from the base model are made optional.

    Args:
        base_model (type[BaseModel]): The original Pydantic model to make partially optional.
        name (str | None, optional): The name of the new model. Defaults to 'Partial{BaseModelName}'.

    Returns:
        type[BaseModel]: A new Pydantic model with all fields from the base model set as optional.
    """
    name = name or f'Partial{base_model.__name__}'
    annotations = get_type_hints(base_model, include_extras=True)

    fields = {field: (Optional[annotation], None) for field, annotation in annotations.items()}

    return create_model(name, __base__=BaseModel, **fields)
