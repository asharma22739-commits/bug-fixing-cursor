# Bug Fixing Using Cursor AI

A buggy Python program identified and corrected using Cursor AI.

| File | Description |
|------|-------------|
| `buggy_code.py` | Original program with three deliberate bugs |
| `fixed_code.py` | Corrected version with `# FIXED:` comments |

## Bugs Found and Fixed

1. Average divided by `len(numbers) + 1` instead of `len(numbers)`.
2. `largest` used `<`, so it returned the minimum instead of the maximum.
3. The first `print` was missing a closing parenthesis.

## Technologies

- Python 3
- Cursor AI

## How to Run

```bash
python buggy_code.py
python fixed_code.py
```
