# Let's create a CSV file and write data to it in Django
import csv

data = [
    {'Name': 'Alice', 'Age': 30},
    {'Name': 'Bob', 'Age': 25},
    {'Name': 'Charlie', 'Age': 35}
]

# Specify the file path
file_path = 'data.csv'

# Write data to the CSV file
with open(file_path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Name', 'Age'])
    writer.writeheader()
    for row in data:
        writer.writerow(row)

# CSV file 'data.csv' is created with the provided data
# Please Like and Subscribe