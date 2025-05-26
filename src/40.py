import os

def delete_file(path):
    try:
        if os.path.exists(path):
            os.remove(path)
            print(f"The file {path} has been deleted.")
        else:
            print(f"The path {path} does not exist.")
    except FileNotFoundError:
        print("The specified file or directory is not found.")
    except Exception as e:
        print(f"An error occurred while deleting the file: {e}")

delete_file("/path/to/your/file.txt")
