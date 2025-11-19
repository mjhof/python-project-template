"""Post-generation hook to clean up and initialize."""
import os
import shutil
from pathlib import Path


def remove_file(filepath: str) -> None:
    """Remove a file if it exists."""
    path = Path(filepath)
    if path.exists():
        path.unlink()


def remove_dir(dirpath: str) -> None:
    """Remove a directory if it exists."""
    path = Path(dirpath)
    if path.exists():
        shutil.rmtree(path)


def main() -> None:
    """Execute post-generation tasks."""
    # Remove LICENSE if proprietary
    if '{{ cookiecutter.license }}' == 'Proprietary':
        remove_file('LICENSE')
    
    # Remove CLI module if not needed
    if '{{ cookiecutter.include_cli }}' == 'no':
        remove_file('src/{{ cookiecutter.package_name }}/cli.py')
    
    # Remove Docker files if not needed
    if '{{ cookiecutter.use_docker }}' == 'no':
        remove_file('Dockerfile')
        remove_file('docker-compose.yml')
        remove_file('.dockerignore')
    
    print()
    print('=' * 60)
    print('🎉 Project {{ cookiecutter.project_name }} created successfully!')
    print('=' * 60)
    print()
    print('Next steps:')
    print('  1. cd {{ cookiecutter.project_slug }}')
    print('  2. git init')
    print('  3. make install-dev')
    print('  4. git add .')
    print('  5. git commit -m "Initial commit"')
    print()
    print('Happy coding! 🚀')
    print()


if __name__ == '__main__':
    main()