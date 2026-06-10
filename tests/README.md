# Test Suite

All unit tests for the Zoo Garden project are located in this directory.

## Running tests

```bash
# From the project root:

# Run all tests
python3 -m pytest

# Run with verbose output (shows each test name)
python3 -m pytest -v

# Run a single test file
python3 -m pytest tests/test_animals.py

# Run tests matching a keyword (e.g. "bird" or "enclosure")
python3 -m pytest -k "bird"

# Run with coverage report
python3 -m pytest --cov=zoo

# Stop on first failure (fast feedback)
python3 -m pytest -x

# Run last failed tests first
python3 -m pytest --failed-first

# Run with rich traceback on failure
python3 -m pytest -v --tb=long
```

## Common pytest flags

> ℹ️ Don't confuse `python3 -m pytest` (Python's `-m` loads the module) with `pytest -m "slow"` (pytest's `-m` filters by marker). They're different flags that happen to share the same letter.

| Flag | Meaning |
|---|---|
| `-v` / `--verbose` | Print individual test names and results |
| `-m MARK` | Mark filter — run tests with a specific `@pytest.mark` decorator (e.g. `pytest -m "slow"`). Note: this is the **pytest** `-m`, not to be confused with `python3 -m pytest` where `-m` is a Python flag that loads a module |
| `-k` | Keyword expression — run tests whose name matches the given string |
| `-x` | Stop after the first failure |
| `--tb=long` | Full traceback for failures |
| `--failed-first` | Run previously failed tests before the rest |
| `--cov=PATH` | Measure code coverage for the given package |
| `-s` | Print stdout/stderr (don't capture output) |
| `--ff` | Same as `--failed-first` |

## Important: running from project root

Always run pytest from the **project root** (`zoo_garden/`), not from inside `tests/`. This ensures the `zoo` package is importable and imports like `from zoo.animals import Animal` work correctly.

If you run from `tests/` directory, imports will break. If you really must run from elsewhere, use:

```bash
python3 -m pytest tests/
```

## Adding new tests

1. Create a file named `test_*.py` in this directory.
2. Write test functions with `def test_*():`.
3. Optionally use `conftest.py` for shared fixtures.

## IDE integration

Both **VS Code** and **PyCharm** detect pytest automatically and show a GUI test explorer with green/red indicators. Just open the project and look for the "Testing" or "Test" tab.
