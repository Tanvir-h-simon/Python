'''
File Handling:
The key function for working with files in Python is the open(filename, mode) function.
There are four different methods (modes) for opening a file:
 "r" - Read - Default value. Opens a file for reading, error if the file does not exist
 "a" - Append - Opens a file for appending, creates the file if it does not exist
 "w" - Write - Opens a file for writing, creates the file if it does not exist
 "x" - Create - Creates the specified file, returns an error if the file exists
 
In addition you can specify if the file should be handled as binary or text mode
 "t" - Text - Default value. Text mode
 "b" - Binary - Binary mode (e.g. images)
'''
# To create a new file in Python, use the open() method, with "x" - Create - will create a file, returns an error if the file exists
f = open("Demo_file.txt", "x")

# Read a file:
f = open("Demo_file.txt")
print(f.read())
# Read a specific file:
f = open(r"E:\Coding\Python\Python- Basics, OOP, File Handling\15. File Handling\data.txt") # r -> raw string. It disables escape sequences.
print(f.read())

# Close a file:
content = open("Demo_file.txt")
print(content.read())
content.close() # If you are not using the with statement, you must write a close statement in order to close the file

# Using the with statement:
with open("Demo_file.txt", "r") as content:
    print(content.read())
    
# Read only parts of the file:
with open("Demo_file.txt") as content:
    print(content.read(10)) # Return the 5 first characters of the file

# Read Lines:
with open("Demo_file.txt") as content:
    print(content.readline()) #  Return one line (first line) by using the readline() method
    print(content.readline())
    print(content.readline())

with open("Demo_file.txt") as content:
    for i in content: # By looping through the lines of the file, we can read the whole file, line by line:
        print(i) 

# Using try-except:
try:
    with open("Demo_file.txt", "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("Error: The file 'Demo_file.txt' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")