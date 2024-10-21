## {{cookiecutter.project_name}}

### Environment Setup
1. Open the project in vscode
1. Ensure you have "Dev Containers" extention installed
1. Go to Command Palette and then run "Dev Containers: Rebuild and Reopen in Container"

### Run Services
1. `docker compose up`

### Run API
{% if cookiecutter.framework == 'django' -%}
1. `python api/manage.py migrate`
1. `python api/manage.py runserver`
{%- endif %}

{% if cookiecutter.include_ui == 'yes' -%}
### Run UI
1. Install node version `nvm install 20`
1. `cd ui`
1. `npm install`
1. `npm run dev`
{%- endif %}
