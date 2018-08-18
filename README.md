# cachedgenerator
Cached generators for python

## Installation

```
pip install cachedgenerator
```

## Usage

```python
from cachedgenerator import cachedgenerator

@cachedgenerator
def a(x):
    yield x

b = a(4)
print list(b)  # [4]
print list(b)  # [4]
```

