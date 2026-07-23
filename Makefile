# .PHONY is used so that the commands are not interpreted as filenames as by default
.PHONY: setup lint format run-dvc run-optuna

setup:
	uv venv # Creates a virtual environment
	uv pip install ".[devops]" # It finds pyproject.toml
	uv run pre-commit install # Wires up Git hooks which automatically check errors and formatting before allowing a commit

lint:
	uv run ruff check src/
	uv run black --check src/

format:
	uv run ruff check --fix src/
	uv run black src/

run-dvc:
	uv run dvc repro

