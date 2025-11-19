"""Core functionality for {{ cookiecutter.project_name }}."""


def hello(name: str = "World") -> str:
    """Return a greeting message.

    Args:
        name: The name to greet. Defaults to "World".

    Returns:
        A greeting message string.
    """
    return f"Hello, {name}!"


def main() -> None:
    """Main entry point for the application."""
    print(hello())


if __name__ == "__main__":
    main()