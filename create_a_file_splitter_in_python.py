# To split a file into smaller parts, we can use the `split` method from the `shutil` module in Python.

# First, we need to import the `shutil` module.
import shutil

# Define the function to split the file.
def split_file(file_path, chunk_size):
    # Open the file in binary mode.
    with open(file_path, 'rb') as file:
        # Read the contents of the file.
        data = file.read()
        
        # Get the total size of the file.
        file_size = len(data)
        
        # Calculate the number of chunks required.
        num_chunks = file_size // chunk_size + 1
        
        # Split the file into chunks.
        for i in range(num_chunks):
            # Calculate the start and end positions for each chunk.
            start = i * chunk_size
            end = min((i + 1) * chunk_size, file_size)
            
            # Create a new file for each chunk.
            chunk_file_path = f'{file_path}.part{i}'
            
            # Write the chunk data to the new file.
            with open(chunk_file_path, 'wb') as chunk_file:
                chunk_file.write(data[start:end])
                
            # Print the file path of each chunk.
            print(f'Split file: {chunk_file_path}')

# Provide the file path and chunk size as inputs.
file_path = input("Enter the file path: ")
chunk_size = int(input("Enter the chunk size (in bytes): "))

# Call the split_file function.
split_file(file_path, chunk_size)

# Please Like and Subscribe