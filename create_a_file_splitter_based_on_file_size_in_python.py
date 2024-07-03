# Let's create a file splitter that splits a file based on size
# No third-party packages needed

def split_file(input_file, chunk_size):
    with open(input_file, 'rb') as f_in:
        chunk_num = 1
        while True:
            chunk = f_in.read(chunk_size)
            if not chunk:
                break
            with open(f'output_chunk_{chunk_num}.txt', 'wb') as f_out:
                f_out.write(chunk)
            chunk_num += 1

# Let's split a file named 'input.txt' into chunks of 100 bytes
split_file('input.txt', 100)
# This will create output files like 'output_chunk_1.txt', 'output_chunk_2.txt'
# Please Like and Subscribe