# Recursion is when a function calls itself.
# Count:
def countdown(n):
    if n <= 0: # Base case
        print("Done!")
    else:
        print(n)
        countdown(n - 1) # Recursive case

countdown(5)
print()

# Factorial:
def factorial(n):
    if n == 0 or n == 1: # Base case
        return 1
    else:
        return n * factorial(n - 1) # Recursive case

print(factorial(5))
print()

# Fibonacci:
def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))
print()

# Recursion with lists:
def sum_list(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + sum_list(numbers[1:])

my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list))

# Recursion Depth Limit:
# Python has a limit on how deep recursion can go. The default limit is usually around 1000 recursive calls.
# Check the recursion limit:
import sys
print(sys.getrecursionlimit())
# If we need deeper recursion, we can increase the limit:
import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())