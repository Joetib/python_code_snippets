# Import the Django model you want to fetch data from
from myapp.models import MyModel
# Fetch all objects from the model
data = MyModel.objects.all()
# Loop through the data and access fields
for obj in data:
    print(obj.field_name)
# Output
# >> value1
# >> value2
# >> value3
# Please Like and Subscribe