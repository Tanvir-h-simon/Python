# To delete a file, you must import the OS module, and run its os.remove() function:
import os
if os.path.exists("Demo_file.txt"):
    os.remove("Demo_file.txt")
    print("File Successfully deleted")
else:
    print("The file does not exist")