# .PHONY is used so that the commands are not interpreted as filenames as by default
.PHONY: setup lint format run-dvc

setup:
	uv venv # Creates a virtual environment
	uv pip install ".[devops]" # It finds pyproject.toml
	uv run pre-commit install # Wires up Git hooks which automatically check errors and formatting before allowing a commit

lint:
	uv run ruff check --fix src/

format:
	uv run black src/

run-dvc:
	uv run dvc repro

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	rm -rf .pytest_cache
	rm -rf models/*

all: setup lint format run-dvc
