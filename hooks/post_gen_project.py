import os
from pprint import pprint

# Get the Cookiecutter configuration
config = {
    "project_name": "{{ cookiecutter.project_name }}",
    "project_slug": "{{ cookiecutter.project_slug }}",
    "include_ui": "{{ cookiecutter.include_ui }}",
    "framework": "{{ cookiecutter.framework }}",
    "use_database": "{{ cookiecutter.use_database }}",
    "database": "{{ cookiecutter.database }}",
    "django_secret_key": "{{ cookiecutter.django_secret_key }}",
}

# Print the configuration
print("\nProject configuration used during generation:")
pprint(config)