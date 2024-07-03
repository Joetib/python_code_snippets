import os

def delete_file(file_path):
    """
    Deletes a file given its file path.
    """
    try:
        os.remove(file_path)
        print(f"File {file_path} deleted successfully.")
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred while deleting the file: {e}")

# Example usage
file_path = input("Enter the file path: ")
delete_file(file_path)
# Please Like and Subscribe