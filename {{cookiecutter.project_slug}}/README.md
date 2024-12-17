## wb test

### Environment Setup
1. Open the project in vscode
1. Ensure you have "Dev Containers" extention installed
1. Go to Command Palette and then run "Dev Containers: Rebuild and Reopen in Container"

### Run Services
1. `docker compose up`

### Run API
{%- if cookiecutter.framework == 'django' %}
1. `python api/manage.py migrate`
1. `python api/manage.py runserver`
{%- endif %}
{%- if cookiecutter.framework == 'fastapi' %}
1. `sh api/scripts/migrate.sh`
1. `uvicorn api.forge.api_app:app --reload --reload-dir api` OR Run from the debugger
{%- endif %}


### Run UI
1. `cd ui`
1. `npm run dev` OR Run from the debugger

### Deployment
1. Create a supabase project
1. Copy the databae URL from supabase
1. Configure the Provider in Supabase Authentication (Google)
1. Configure the Site URL in URL Configuration under Authentication
1. Create a CloudAMQP account and a RabbitMQ queue, and get the broker URL
1. Create a project in Render 
1. Deploy the backend on Render and set the environment variables
1. Copy the API endpoint
1. Deploy the frontend on Vercel and get the endpoint