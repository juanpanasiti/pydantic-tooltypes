# Pydantic Tooltypes

TypeScript-like utilities for Pydantic models: `Partial`, `Pick`, `Omit`, and `Required`.

## Features

- `Partial`: Makes all fields in a Pydantic model optional.
- `Pick`: Selects a subset of fields from a model.
- `Omit`: Removes a subset of fields from a model.
- `Required`: Makes selected fields required, others optional.

All utilities now support **class parametrization**, similar to generics in TypeScript or Python typing.

## Installation

```bash
pip install pydantic-tooltypes
```

## Usage

```python
from pydantic import BaseModel
from pydantic_tooltypes import Partial, Pick, Omit, Required

class User(BaseModel):
    id: int
    email: str

# Partial: all fields optional
PartialUser = Partial[User]

# Pick: only selected fields included (and required)
PickUser = Pick[User, ['email']]

# Omit: all except the listed fields (the rest are required)
OmitUser = Omit[User, ['id']]

# Required: make some fields required over a Partial model
RequiredUser = Required[PartialUser, ['email']]
```

## License

MIT
