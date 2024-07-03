# In Django, we can send a JSON response using JsonResponse
from django.http import JsonResponse

data = {'key': 'value'}
# Return JSON response with data
return JsonResponse(data)

# This will send a JSON response with {'key': 'value'}
# Please Like and Subscribe