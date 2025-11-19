sentence = "Hello, World"
print(sentence[2:5]) # The first character has index 0

# Slice from the start
b = "Hello, World!"
print(b[:5]) # Get the characters from the start to position 5 (not included)

# Slice from the end
b = "Hello, World!"
print(b[2:]) # Get the characters from position 2, and all the way to the end

# Negative indexing: Use negative indexes to start the slice from the end of the string
b = "Hello, World!"
print(b[-5:-2])