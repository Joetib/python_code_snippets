# Json is a common format for sharing data between applications
# Let's learn how to parse it using the builtin 'json' module

import json

sample_json_text  = """{ "id": 189, "Name": "Oti", "Nationality": "Ghanaian" }"""

# Let's convert it into a python data structure
parsed_data = json.loads(sample_json_text)

print(parsed_data)
# OUTPUT >>> {'id': 189, 'Name': 'Oti', 'Nationality': 'Ghanaian'}

print(type(parsed_data))
# OUTPUT >>> <class 'dict'>