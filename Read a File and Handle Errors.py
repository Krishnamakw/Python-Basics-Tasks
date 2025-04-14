# Task 7: Read a File and Handle Errors

try:
    # Open and read the file
    with open("sample.txt", "r") as file:
        print("File contents:\n")
        for line in file:
            print(line.strip())  # .strip() removes newline characters
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
