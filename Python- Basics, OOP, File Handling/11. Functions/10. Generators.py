# Generators are functions that can pause and resume their execution.
# When a generator function is called, it returns a generator object, which is an iterator.
# A generator is a function that produces values one at a time, instead of building the entire result in memory. It uses the yield keyword instead of return.
def generator_func():
    yield 1 # Uses the 'yield' keyword instead of 'return'
    yield 2
    yield 3

for value in generator_func():
    print(value,end=" ")
print()
    

def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for num in count_up_to(5):
    print(num,end=" ")

# Generators are memory-efficient because they generate values on-the-fly instead of storing everything in memory.
# For large datasets, generators save memory:
def large_sequence(n):
    for i in range(n):
        yield i

gen = large_sequence(1000000) # This doesn't create a million numbers in memory
print(next(gen))
print(next(gen))
print(next(gen))
print()

# When there are no more values to yield, the generator raises a StopIteration exception:
def simple_gen():
    yield 1
    yield 2

gen = simple_gen()
print(next(gen))
print(next(gen))
# print(next(gen)) # This will raise StopIteration

# Get first 100 Fibonacci numbers
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fibonacci()
for _ in range(100):
    print(next(gen))

# Generator method:
# next() method:
def gen():
    yield 1
    yield 2

g = gen()
print(next(g)) 
print(next(g))

# send() Method:
def greeter():
    name = yield "Ready" 
    yield f"Hello, {name}"

g = greeter()
print(next(g)) 
print(g.send("Tanvir"))

# close() Method:
def numbers():
    try:
        yield 1
        yield 2
        yield 3
    except GeneratorExit:
        print("Generator closed")

g = numbers()
print(next(g)) 
g.close()