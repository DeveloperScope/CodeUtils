# CodeUtils Core

CodeUtils Core is a lightweight utility library designed to support core operations in arithmetic, string manipulation, data serialization, and basic I/O functionality. It is intended for internal use in backend services and developer tools that require modular, single-responsibility components.

## Features

- Arithmetic operations (add, subtract, multiply, divide, modulo, power, factorial)
- String transformations (case conversion, reversal)
- List flattening utility
- Lightweight HTTP client
- Simple file server interface
- Serialization helpers

## Requirements

- Python 3.8+

Some components may require optional dependencies like `requests`.

## Usage

Each module provides a single function and can be imported independently. Example:

```python
from calc_add import add

result = add(5, 3)
print(result)  # Output: 8
```