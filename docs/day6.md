### Day 06:
Linters

For ensuring code quality, we are going to utilize Ruff and Black.
`Black` is only a formatter, whereas `Ruff` is a linter/formatter.
The first only adjustst the code to conform with the universal style
requirements and has minimal adjustable settings.
The later does linting - scanning the code for bugs, logic errors, etc. -
and formats the code like `Black`.
Historically they were used together, but Ruff has a Black-compatible formatter
which makes concurrent usage unecessary. I'm leaving both in though for reference
and to provide the user with the choice to decide.

You can try them out with:
```
# linter in safe mode
ruff check src/
# linter
ruff check --fix src/
# formatter in safe mode
ruff format --check src/
# formatter
ruff format src/
```
and
```
# safe mode
black --check src/
# live
black src/
```

Please observe the setting in `pyproject.toml`.
The linters will automatically check this file and grab the settings from it.
In case of ruff, we are applying four rules:
"W" - style warnings (structural style issues and syntax errors - whitespace, line breaaks, etc)
"E" - style errors (enforcing the PEP style guide)
"F" - Pyflakes linter (logical errors and bugs)
"I" - isort (sorting and groping imports)
