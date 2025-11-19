try:
    x = int(input("Enter a number: ")) # The try block test a block of code for errors.
    result = 10 / x
except ValueError:
    print("Invalid input. Please enter a valid integer.") # The except block handle the error.
except ZeroDivisionError:
    print("You cannot divide by zero.")
else:
    print("Success! Result =", result) # The else block execute code when there is no error.
finally:
    print("Execution completed.") # The finally block0 execute code, regardless of the result of the try- and except blocks.