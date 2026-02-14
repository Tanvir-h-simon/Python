# sentence = input()
# print(sentence)
# sentence = input("Enter a sentence: ")
# print("Output:", sentence)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a + b)

# a = float(input())
# b = float(input())
# print(a + b)

# Multiple inputs in one line:
# sentence = input().split() # Python is Fun
# print(sentence) # ['Python', 'is', 'Fun'] -> A list of strings

a, b = map(int, input("Enter two numbers: ").split()) # map(function, iterable)
print(a + b)

# print("Enter your name:")
# name = input()
# print(f"Hello {name}")

name = input("Enter your name:")
print(f"Hello {name}")

name = input("Enter your name:")
print(f"Hello {name}")
fav1 = input("What is your favorite animal:")
fav2 = input("What is your favorite color:")
fav3 = input("What is your favorite number:")
print(f"Do you want a {fav2} {fav1} with {fav3} legs?")