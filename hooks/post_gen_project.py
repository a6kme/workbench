import os
import shutil

is_django = '{{cookiecutter.framework}}' == 'django'
is_fastapi = '{{cookiecutter.framework}}' == 'fastapi'
include_ui = '{{cookiecutter.include_ui}}' == 'yes'

assert is_django or is_fastapi

if is_django:
    # remove api_fastapi directory and rename api_django to api
    shutil.rmtree('api_fastapi')
    os.rename('api_django', 'api')

if is_fastapi:
    # remove api_django directory and rename api_fastapi to api
    shutil.rmtree('api_django')
    os.rename('api_fastapi', 'api')

if not include_ui:
    shutil.rmtree('ui')

# change the permissions of .devcontainer/setup.sh to be executable
os.chmod('.devcontainer/setup.sh', 0o755)

print("Project initialized successfully! Happy building!!")
