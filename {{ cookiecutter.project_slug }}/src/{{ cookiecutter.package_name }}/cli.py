"""Command-line interface for {{ cookiecutter.project_name }}."""
{% if cookiecutter.include_cli == "yes" %}
import argparse

from {{ cookiecutter.package_name }}.core import hello


def main() -> None:
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="{{ cookiecutter.project_description }}"
    )
    parser.add_argument(
        "name",
        nargs="?",
        default="World",
        help="Name to greet",
    )
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 0.1.0",
    )
    
    args = parser.parse_args()
    print(hello(args.name))


if __name__ == "__main__":
    main()
{% endif %}