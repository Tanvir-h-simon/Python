# F-string allows to format selected parts of a string.
# To specify a string as an f-string, simply put an f in front of the string literal.

price = 59.453
# txt = f"The price is {price} dollars"
# print(txt)
txt = "The price is {} dollars"
print(txt.format(price))

print(f"The price is {price:.2f} dollars")

txt = f"The price is {20 * 59} dollars"
print(txt)

price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)

fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# Use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))