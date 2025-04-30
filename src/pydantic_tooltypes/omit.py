from typing import get_type_hints
from pydantic import BaseModel, create_model


def Omit(base_model: type[BaseModel], keys: list[str], name: str | None = None) -> type[BaseModel]:
    """
    Creates a new Pydantic model excluding specific fields from the base model.

    Args:
        base_model (type[BaseModel]): The original Pydantic model to omit fields from.
        keys (list[str]): The list of field names to exclude from the new model.
        name (str | None, optional): The name of the new model. Defaults to 'Omit{BaseModelName}'.

    Returns:
        type[BaseModel]: A new Pydantic model without the specified fields.
    """
    name = name or f'Omit{base_model.__name__}'
    annotations = get_type_hints(base_model, include_extras=True)

    fields = {k: (annotation, ...) for k, annotation in annotations.items()if k not in keys}

    return create_model(name, __base__=BaseModel, **fields)
