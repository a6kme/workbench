import os
import re
import shutil
import secrets

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

django_secret_key = secrets.token_urlsafe(32)
superuser_password = secrets.token_urlsafe(8)


# Helper function to find and replace text in a file
def find_and_replace_in_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    # Replace the old text with new text using regex
    new_content = re.sub('____SUPERUSER_PASSWORD____', superuser_password, content)
    new_content = re.sub('____DJANGO_SECRET_KEY____', django_secret_key, new_content)

    # Write the new content back to the file if there's any change
    if new_content != content:
        with open(file_path, "w") as file:
            file.write(new_content)

# Walk through the entire project directory
def replace_in_project(directory):
    FILE_EXTENSIONS = [".py", ".env"]
    for root, _, files in os.walk(directory):
        for file in files:
            file_ext = os.path.splitext(file)[1] or file # in case we have a dot file
            if file_ext in FILE_EXTENSIONS:
                file_path = os.path.join(root, file)
                find_and_replace_in_file(file_path)

# Entry point: Post-generation hook
if __name__ == "__main__":
    project_directory = os.getcwd()  
    replace_in_project(project_directory)


print("Superuser created with admin: admin and password: {}".format(superuser_password))
print("Project initialized successfully! Happy building!!")
