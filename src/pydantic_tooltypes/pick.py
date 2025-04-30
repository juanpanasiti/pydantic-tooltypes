from typing import get_type_hints
from pydantic import BaseModel, create_model


def Pick(base_model: type[BaseModel], keys: list[str], name: str | None = None) -> type[BaseModel]:
    """
    Creates a new Pydantic model by selecting a subset of fields from the given base model.

    Args:
        base_model (type[BaseModel]): The original Pydantic model to pick fields from.
        keys (list[str]): A list of field names to include in the new model.
        name (str | None, optional): The name of the new model. Defaults to 'Pick{BaseModelName}'.

    Returns:
        type[BaseModel]: A new Pydantic model including only the specified fields, all required.
    """
    name = name or f'Pick{base_model.__name__}'
    annotations = get_type_hints(base_model, include_extras=True)

    fields = {k: (annotations[k], ...)for k in keys if k in annotations}

    return create_model(name, __base__=BaseModel, **fields)
