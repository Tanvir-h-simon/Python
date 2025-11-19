# JSON (JavaScript Object Notation) is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.

# Conevert JSON to Python: We can parse it by using the json.loads() method
import json

x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x) # parse x to python
print(y["age"])

# Convert from Python to JSON: We can convert it into a JSON string by using the json.dumps() method
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
y = json.dumps(x) # convert into JSON
print(y)
# Other data types:
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))