.PHONY: help install install-dev sync update clean test test-cov lint format check pre-commit run build

.DEFAULT_GOAL := help

help: ## Show this help message
	@echo "Usage: make [target]"
	@echo ""
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install production dependencies
	uv sync --no-dev

install-dev: ## Install all dependencies including dev
	uv sync --all-extras
	uv run pre-commit install

sync: ## Sync dependencies with lock file
	uv sync

update: ## Update dependencies
	uv lock --upgrade
	uv sync

clean: ## Clean build artifacts and cache
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache/
	rm -rf .ruff_cache/
	rm -rf htmlcov/
	rm -rf .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

test: ## Run tests
	uv run pytest

test-cov: ## Run tests with coverage report
	uv run pytest --cov=src --cov-report=html --cov-report=term-missing

lint: ## Run ruff linter
	uv run ruff check .

format: ## Run ruff formatter
	uv run ruff format .

check: ## Run all checks (lint + format check)
	uv run ruff check .
	uv run ruff format --check .

pre-commit: ## Run pre-commit on all files
	uv run pre-commit run --all-files

pre-commit-update: ## Update pre-commit hooks
	uv run pre-commit autoupdate

{% if cookiecutter.include_cli == "yes" -%}
run: ## Run the main application
	uv run {{ cookiecutter.project_slug }}
{% else -%}
run: ## Run the main application
	uv run python -m {{ cookiecutter.package_name }}
{% endif %}

build: ## Build package
	uv build

publish: ## Publish package to PyPI
	uv publish

ci: lint check test ## Run all CI checks locally