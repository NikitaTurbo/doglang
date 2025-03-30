import sys
from interpreter import DogLangInterpreter as dg

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <file.dog>")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            code = file.read()
        dg().execute(code)
    except FileNotFoundError:
        print(f"File {filename} not found.")
        sys.exit(1)
