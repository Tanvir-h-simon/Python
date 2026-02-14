'''
Python divides the operators in the following groups:
Arithmetic operators: +, -, *, /, %, **, //
Assignment operators: =, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=
Comparison operators: ==, !=, >, <, >=, <=
Logical operators: and, or, not
Identity operators: is, is not
Membership operators: in, not in
Bitwise operators: &, |, ^, ~, <<, >>
'''
# Arithmetic operators
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y) # returns a floot
print(x % y)
print(x ** y) # Exponentiation -> x^y
print(x // y) # Floor division(It rounds DOWN to the nearest integer), returns an integer (integer division in C, C++ or java, such as 15 / 4 = 3)

'''
Precendence order: () > ** > +x -x ~x > * / // % > + - > << >> > & > ^ > | > == != > >= < <= is is not in not in > not > and > or
'''