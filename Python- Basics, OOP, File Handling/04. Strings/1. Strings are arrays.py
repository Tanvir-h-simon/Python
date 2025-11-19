# strings in Python are arrays of unicode characters
# Python does not have a character data type, a single character is simply a string with a length of 1
a = "Hello, World!"
print(a[1])

a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")
    
txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")
    
# Loop through a string
for x in "banana":
    print(x, end=" ")
print()

# string length
print(len("banana")) 