# Lets split a file into chunks

def split_file(file_path, chunk_size):
    # Open the file in binary mode.
    with open(file_path, 'rb') as file:
        data = file.read()
        file_size = len(data)
        # Calculate the number of chunks required.
        num_chunks = file_size // chunk_size + 1
        for i in range(num_chunks):
            start = i * chunk_size
            end = min((i + 1) * chunk_size, file_size)
            chunk_file_path = f'{file_path}.part{i}'
            with open(chunk_file_path, 'wb') as chunk_file:
                chunk_file.write(data[start:end])
            print(f'Split file: {chunk_file_path}')

file_path = input("Enter the file path: ")
chunk_size = int(input("Enter the chunk size (in bytes): "))

split_file(file_path, chunk_size)
# Please Like and Subscribe