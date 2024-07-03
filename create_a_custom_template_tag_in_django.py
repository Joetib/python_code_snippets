# Create a custom template tag in Django to display current date
# Create a folder 'templatetags' in your app directory
# Inside 'templatetags' folder, create a file e.g. custom_tags.py

from django import template
from datetime import datetime

register = template.Library()

@register.simple_tag
def current_date():
    return datetime.now().strftime('%Y-%m-%d')

# In your template, load the custom tag at the top
# {% load custom_tags %}
# Then, use the custom tag to display current date
# {% current_date %}

# Output
# 2022-01-01
# Please Like and Subscribe