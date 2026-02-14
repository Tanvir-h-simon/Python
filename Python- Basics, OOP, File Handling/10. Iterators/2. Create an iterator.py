# To create an object/class as an iterator we have to implement the methods __iter__() and __next__() to our object.
# The __iter__() method acts similar, we can do operations (initializing etc.), but must always return the iterator object itself.
# The __next__() method also allows we to do operations, and must return the next item in the sequence.
class numbers:
    def __iter__(self):
        self.a = 1
        return self
    
    # def __next__(self):
    #     x = self.a
    #     self.a += 1
    #     return x
    # The example above would continue forever if we had enough next() statements, or if it was used in a for loop.
    # To prevent the iteration from going on forever, we can use the StopIteration statement.
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
    
my_class = numbers()
it = iter(my_class)

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
for x in it:
    print(x, end=" ")