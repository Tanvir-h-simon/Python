# An iterator is an object that contains a countable number of values.
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
# Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().

# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which we can get an iterator from.
this_tuple = ("apple", "banana", "cherry")
it = iter(this_tuple)
# print(next(it))
# print(next(it))
# print(next(it))
# for i in range(len(this_tuple)):
#     print(next(it), end=" ")
# print(i)
for i in this_tuple:
    print(i)

# Even strings are iterable objects, containing a sequence of characters, and can return an iterator
str = "banana"
it = iter(str)
# print(next(it), end=" ")
# print(next(it), end=" ")
# print(next(it), end=" ")
# print(next(it), end=" ")
# print(next(it), end=" ")
# print(next(it), end=" ")\
# for i in range(len(str)):
#     print(next(it), end=" ")
for i in str:
    print(i, end=" ")