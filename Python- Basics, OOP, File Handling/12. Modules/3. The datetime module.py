import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))

# Creating a date object
x = datetime.datetime(2020, 5, 17)
print(x)

# The strftime() Method
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B")) # %B- Month name
print(x.strftime("%A")) # %A- Weekday
print(x.strftime("%d")) # Day of month 01-31