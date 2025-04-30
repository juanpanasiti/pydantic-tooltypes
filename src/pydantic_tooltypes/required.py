from typing import get_type_hints
from pydantic import BaseModel, create_model


def Required(base_model: type[BaseModel], keys: list[str], name: str | None = None) -> type[BaseModel]:
    """
    Creates a new Pydantic model from the base model, making only the specified fields required
    while keeping all other fields optional.

    Args:
        base_model (type[BaseModel]): The original Pydantic model to derive from.
        keys (list[str]): The list of field names that should be required in the new model.
        name (str | None, optional): The name of the new model. Defaults to 'Required{BaseModelName}'.

    Returns:
        type[BaseModel]: A new Pydantic model with selected required fields.
    """
    name = name or f'Required{base_model.__name__}'
    annotations = get_type_hints(base_model, include_extras=True)

    fields = {}
    for k, annotation in annotations.items():
        if k in keys:
            fields[k] = (annotation, ...)
        else:
            fields[k] = (annotation, None)

    return create_model(name, __base__=BaseModel, **fields)
