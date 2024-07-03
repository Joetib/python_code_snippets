# To create a file compressor in Python, we can use the `gzip` module which is a built-in module in Python.

# First, we need to import the `gzip` module.
import gzip
input_file = "input.txt"
output_file = "compressed.gz"
# Now, we can open the input file in read mode and the output file in write mode.
# Then, we can use the `gzip.open()` function to create a gzip file object for writing.
with open(input_file, 'rb') as file_in, gzip.open(output_file, 'wb') as file_out:
    # We can then use a loop to read the input file in chunks and write the compressed data to the output file.
    # We can use a chunk size of 1024 bytes, but you can adjust it according to your needs.
    chunk_size = 1024
    while True:
        chunk = file_in.read(chunk_size)
        if not chunk:
            break
        file_out.write(chunk)

# Finally, we can print a message to indicate that the compression process is complete.
print("File compression complete.")
# Output:
# File compression complete.
# Please Like and Subscribe