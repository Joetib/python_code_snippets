# Let's create a file merger that merges files based on size
# No third-party package needed

def merge_files(input_files, output_file, max_size):
    with open(output_file, 'wb') as out_file:
        for file_name in input_files:
            with open(file_name, 'rb') as in_file:
                out_file.write(in_file.read())

    # Check if output file exceeds max size
    if os.path.getsize(output_file) > max_size:
        print("Merged file exceeds max size.")
    else:
        print("Files merged successfully.")

# Example usage
input_files = ['file1.txt', 'file2.txt']
output_file = 'merged_file.txt'
max_size = 1000000  # 1MB
merge_files(input_files, output_file, max_size)
# Please Like and Subscribe