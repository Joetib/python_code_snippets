# Create a custom management command in Django
# 1. Create a 'management' folder in your app directory
# 2. Inside 'management' folder, create 'commands' folder
# 3. Inside 'commands' folder, create a Python file, e.g., 'my_command.py'
# 4. Define a class that extends BaseCommand from django.core.management.base
# 5. Implement handle() method in the class to define the command logic

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Custom management command example'

    def handle(self, *args, **options):
        self.stdout.write('Running custom command...')
        # Add your custom command logic here

# To run the custom command, use:
# >> python manage.py my_command
# Please Like and Subscribe