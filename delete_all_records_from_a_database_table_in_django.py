# Import the model from which you want to delete records
from myapp.models import MyModel
# Delete all records from the table
MyModel.objects.all().delete()
# Please Like and Subscribe