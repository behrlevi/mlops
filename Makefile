.PHONY: setup lint format run-dvc run-optuna

setup:
	uv venv
	uv pip install -r pyproject.toml
	pre-commit install

lint:
	ruff check src/
	black --check src/

format:
	ruff check --fix src/
	black src/

run-dvc:
	dvc repro
