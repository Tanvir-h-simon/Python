'''
To write to an existing file, you must add a parameter to the open() function:
 "a" - Append - will append to the end of the file
 "w" - Write - will overwrite any existing content
'''
'''
To create a new file in Python, use the open() method, with one of the following parameters:
 "x" - Create - will create a file, returns an error if the file exists
 "a" - Append - will create a file if the specified file does not exists
 "w" - Write - will create a file if the specified file does not exists
'''

# Write to an Existing File:
with open("Demo_file.txt", "a") as content:
    content.write("\nNow the file has more content!")
with open("Demo_file.txt", "r") as content: # open and read the file after the appending
    print(content.read())

# Overwrite Existing Content:
with open("Demo_file.txt", "w") as content:
    content.write("Woops! I have deleted the content!")
with open("Demo_file.txt", "r") as content: # open and read the file after the overwriting
    print(content.read())