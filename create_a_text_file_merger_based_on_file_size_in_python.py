# Let's create a text file merger based on file size
# First, we need to install the 'filechunkio' library
# >> pip install filechunkio

import filechunkio

def merge_files(input_files, output_file, chunk_size):
    with open(output_file, 'wb') as output:
        for input_file in input_files:
            with open(input_file, 'rb') as file:
                chunk = file.read(chunk_size)
                while chunk:
                    output.write(chunk)
                    chunk = file.read(chunk_size)

# Example usage
input_files = ['file1.txt', 'file2.txt']
output_file = 'merged_file.txt'
chunk_size = 1024  # 1KB
merge_files(input_files, output_file, chunk_size)
# Please Like and Subscribe