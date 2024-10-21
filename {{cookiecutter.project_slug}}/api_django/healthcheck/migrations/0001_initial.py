from django.db import migrations
from django.contrib.auth.models import User

def create_superuser(apps, schema_editor):
    # Create a superuser if it doesn't already exist
    User = apps.get_model('auth', 'User')
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='{{cookiecutter.superuser_email}}',
            password='____SUPERUSER_PASSWORD____',
        )

def delete_superuser(apps, schema_editor):
    # Optionally, define how to reverse the migration (e.g., delete the superuser)
    User = apps.get_model('auth', 'User')
    User.objects.filter(username='admin').delete()

class Migration(migrations.Migration):

    dependencies = [
        # Ensure you depend on the migration that created the User model
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.RunPython(create_superuser, reverse_code=delete_superuser),
    ]