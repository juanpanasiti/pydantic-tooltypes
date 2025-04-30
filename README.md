# Pydantic Tooltypes

TypeScript-like utilities for Pydantic models: `Partial`, `Pick`, `Omit`, and `Required`.

## Features

- `Partial`: Makes all fields in a Pydantic model optional.
- `Pick`: Selects a subset of fields from a model.
- `Omit`: Removes a subset of fields from a model.
- `Required`: Makes selected fields required, others optional.

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

PartialUser = Partial(User)
PickUser = Pick(User, keys=['email'])
OmitUser = Omit(User, keys=['id'])
RequiredUser = Required(PartialUser, keys=['email'])
```

## License

MIT
