# Let's create a function to split a text file based on size
# No external libraries needed

def split_text_file(input_file, max_size):
    with open(input_file, 'r') as file:
        data = file.read()
    
    chunks = [data[i:i+max_size] for i in range(0, len(data), max_size)]
    
    for i, chunk in enumerate(chunks):
        with open(f'{input_file}_part{i+1}.txt', 'w') as file:
            file.write(chunk)

# Example usage
split_text_file('input.txt', 1000)
# This will split 'input.txt' into parts of 1000 characters each
# Please Like and Subscribe