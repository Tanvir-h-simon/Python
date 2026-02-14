# map(function, iterable)- map() applies a function to every item in an iterable and returns the iterator
str_num = ["1", "2", "3", "4", "5"]
int_num = map(int, str_num)
print(list(int_num))

words = ["hello", "world", "python"]
uppercase = list(map(str.upper, words))
print(uppercase)

words = ["hi", "hello", "hey"]
lengths = list(map(len, words))
print(lengths)

# Without lambda function:
def square(num):
    return num * num

numbers = [1, 2, 3, 4, 5]
squared = list(map(square, numbers))
print(squared)

# Lambda function:
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda num: num * num, numbers))
print(squared)

# filter(function, iterable)- The function should return True or False. Items that return True are kept, others are filtered out.
def is_even(num):
    return num % 2 == 0

num_list = [1, 2, 3, 4, 5, 6]
result = filter(is_even, num_list) # Items that return True are kept, others are filtered out.
# print((result)) # Returns the iterator
print(list(result))

def long_word(word):
    return len(word) > 3

word_list = ["cat", "apple", "dog", "banana"]
result = list(filter(long_word, word_list))
print(result)

# Using Lambda with filter():
numbers = [1, 2, 3, 4, 5, 6]
even_num = list(filter(lambda num: num % 2 == 0, numbers))
print(even_num)

# sorted()- sorted(iterable, key=None, reverse=False)
numbers = [5, 2, 9, 1, 7]
result = sorted(numbers)
# rev_result = sorted(numbers, reverse=True)
result = sorted(numbers)
print(result)

words = ["banana", "apple", "cherry"]
result = sorted(words) # Alphabetically
print(result)

# Without lambda function
numbers = [5, 2, 9, 1, 7]
def sorted_numbers(x):
    return sorted(x)

print(sorted_numbers(numbers))

# With lambda function
numbers = [5, 2, 9, 1, 7]
sorted_numbers = sorted(numbers, key=lambda x: x)
print(sorted_numbers)

words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x)) # Sort the string by length
print(sorted_words)

students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)] 
sorted_students = sorted(students, key=lambda x: x[1]) # Sort a list of tuples by the second element
print(sorted_students)

data = [(3, 5), (1, 2), (2, 8)] 
result = sorted(data, key=lambda x: x[0]) # Sort by first element
print(result)