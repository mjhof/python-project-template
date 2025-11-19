"""Pre-generation hook to validate input."""
import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

project_slug = '{{ cookiecutter.project_slug }}'
package_name = '{{ cookiecutter.package_name }}'

if not re.match(MODULE_REGEX, package_name):
    print(f'ERROR: {package_name} is not a valid Python module name!')
    print('Please use only letters, numbers and underscores.')
    sys.exit(1)

if project_slug.startswith('-') or project_slug.endswith('-'):
    print(f'ERROR: {project_slug} cannot start or end with a hyphen!')
    sys.exit(1)