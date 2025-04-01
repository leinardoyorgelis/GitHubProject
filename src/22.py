import sys

def main():
    if len(sys.argv) == 2 and sys.argv[1] == '-h' or '-help':
        print("Usage: python script.py <option>")
        exit(0)
    
    if len(sys.argv) != 3:
        print("Error: Please provide exactly one argument, which is the name of the program.")
        exit(1)

if __name__ == "__main__":
    main()
