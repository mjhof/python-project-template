# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Setup

### Prerequisites

- Python {{ cookiecutter.python_version }}+
- [uv](https://github.com/astral-sh/uv) package manager

### Installation

```bash
# Install development dependencies and setup pre-commit hooks
make install-dev
```

## Development

### Common Commands

```bash
make help          # Show all available commands
make format        # Format code with ruff
make lint          # Lint code with ruff
make test          # Run tests
make test-cov      # Run tests with coverage
make ci            # Run all CI checks locally
make clean         # Clean build artifacts
```

### Running the Application

```bash
make run
{% if cookiecutter.include_cli == "yes" -%}
# or
{{ cookiecutter.project_slug }} --help
{% else -%}
# or
uv run python -m {{ cookiecutter.package_name }}
{% endif %}
```

### Running Tests

```bash
# Run all tests
make test

# Run with coverage
make test-cov

# Run specific test file
uv run pytest tests/test_core.py

# Run tests matching a pattern
uv run pytest -k "test_function_name"
```

## Project Structure

```
{{ cookiecutter.project_slug }}/
├── src/{{ cookiecutter.package_name }}/    # Source code
├── tests/                                   # Test files
├── .github/                                 # GitHub Actions workflows
├── Makefile                                 # Common development commands
└── pyproject.toml                           # Project configuration
```

## Contributing

1. Install development dependencies: `make install-dev`
2. Create a feature branch
3. Make your changes
4. Run checks: `make ci`
5. Commit and push (pre-commit hooks will run automatically)
6. Open a pull request

## Author

{{ cookiecutter.author_name }} ({{ cookiecutter.author_email }})

## License

{% if cookiecutter.license != "Proprietary" -%}
{{ cookiecutter.license }}
{% else -%}
Proprietary - All rights reserved
{% endif %}
```

---

## `{{ cookiecutter.project_slug }}/src/{{ cookiecutter.package_name }}/__init__.py`

```python
"""{{ cookiecutter.project_name }} - {{ cookiecutter.project_description }}"""

__version__ = "0.1.0"
```
