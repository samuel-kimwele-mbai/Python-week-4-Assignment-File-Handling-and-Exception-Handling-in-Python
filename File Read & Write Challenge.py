try:
    with open("initial.txt", "r") as file:
        content = file.read()

    modified_content = content.upper()

    with open("modified.txt", "w") as new_file:
        new_file.write(modified_content)

    print("File modified and saved as 'modified.txt'")
except FileNotFoundError:
    print("The file 'initial.txt' was not found.")
except IOError:
    print("Error: Could not read or write to the file.")
