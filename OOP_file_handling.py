# file_handling_assignment.py

# Create a new text file named "my_file.txt" in write mode ('w')
with open("my_file.txt", "w") as my_file:
    # Write at least three lines of text to the file, including a mix of strings and numbers
    my_file.write("Hello, World!\n")
    my_file.write("This is a line with number: 42\n")
    my_file.write("Another line with a different number: 13\n")

# Read the contents of "my_file.txt" and display them on the console
try:
    with open("my_file.txt", "r") as my_file:
        print("File contents:")
        for line in my_file:
            print(line.strip())
except FileNotFoundError:
    print("Error: File 'my_file.txt' not found.")

# Modify the script to open "my_file.txt" in append mode ('a')
# Append three additional lines of text to the existing content
with open("my_file.txt", "a") as my_file:
    my_file.write("Added a new line in append mode!\n")
    my_file.write("This is the second line appended.\n")
    my_file.write("The last line appended to the file.\n")

# Error Handling: Implement error handling using try, except, and finally blocks
print("\nError handling example:")
try:
    with open("non_existent_file.txt", "r") as non_existent_file:
        print("File contents:")
        for line in non_existent_file:
            print(line.strip())
except FileNotFoundError:
    print("Error: File 'non_existent_file.txt' not found.")
except PermissionError:
    print("Error: You do not have permission to read the file.")
except Exception as e:
    print("Unexpected error:", str(e))
finally:
    print("The 'try except' block has been executed.")