# Using Django's slugify function to create a unique slug
# from a model instance's field
# Ensure to import slugify from django.utils.text

from django.utils.text import slugify
from myapp.models import MyModel

instance = MyModel.objects.get(pk=1)
# Let's create a unique slug from the instance's title field
slug = slugify(instance.title)
# Output
# >> 'unique-slug-from-title'
# Please Like and Subscribe