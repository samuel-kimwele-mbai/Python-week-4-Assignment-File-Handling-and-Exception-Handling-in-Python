filename = input("Enter the filename to read: ")

try:
    with open(filename, "r") as user_file:
        data = user_file.read()
        print("\n File Content:\n")
        print(data)

except FileNotFoundError:
    print(f"File '{filename}' not found.")
except PermissionError:
    print(f"Permission denied to read '{filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
