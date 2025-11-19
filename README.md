# Python Project Template

A modern Python project template using Cookiecutter with uv, ruff, and pre-commit.

## Features

- 🚀 Fast dependency management with [uv](https://github.com/astral-sh/uv)
- 🎨 Code formatting and linting with [ruff](https://github.com/astral-sh/ruff)
- 🪝 Pre-commit hooks configured
- 🧪 Testing with pytest
- 📦 Modern pyproject.toml configuration
- 🔄 GitHub Actions CI/CD
- 📝 Comprehensive Makefile
- 🎯 Multiple Python version support
- 📄 Multiple license options
- 🎛️ Optional CLI support

## Usage

### Install Cookiecutter

```bash
pip install cookiecutter
```

### Create a New Project

```bash
# From GitHub
cookiecutter gh:yourusername/python-project-template

# From local directory
cookiecutter /path/to/python-project-template
```

### Answer the Prompts

You'll be asked for:
- **project_name**: Your project name (e.g., "My Awesome Project")
- **project_slug**: Auto-generated from project_name (e.g., "my-awesome-project")
- **package_name**: Auto-generated from project_slug (e.g., "my_awesome_project")
- **project_description**: Brief description of your project
- **author_name**: Your name
- **author_email**: Your email
- **github_username**: Your GitHub username
- **python_version**: Python version (3.11, 3.12, or 3.13)
- **license**: License type (MIT, Apache-2.0, GPL-3.0, BSD-3-Clause, or Proprietary)
- **include_cli**: Whether to include CLI support (yes/no)
- **use_docker**: Whether to include Docker files (yes/no)

### Initialize Your Project

```bash
cd your-project-name
git init
make install-dev
git add .
git commit -m "Initial commit"
```

## What You Get

```
your-project/
├── src/your_package/       # Your Python package
├── tests/                  # Test files with pytest
├── .github/workflows/      # CI/CD with GitHub Actions
├── Makefile               # Development commands
├── pyproject.toml         # Project configuration
├── .pre-commit-config.yaml # Pre-commit hooks
└── README.md              # Project documentation
```

## Development Workflow

```bash
make format        # Format code
make lint          # Lint code
make test          # Run tests
make ci            # Run all checks (like CI does)
```

## Customization

You can customize the template by:
1. Modifying `cookiecutter.json` to add/remove prompts
2. Editing files in `{{ cookiecutter.project_slug }}/`
3. Adding custom hooks in `hooks/`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - feel free to use this template for any project!
```
