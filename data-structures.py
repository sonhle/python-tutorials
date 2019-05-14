# MOre on lists
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits)
print(fruits.count('apple'))
print(fruits.index('banana'))
print(fruits.index('banana', 4))
fruits.reverse()
print(fruits)
fruits.append('grape')
print(fruits)
fruits.sort()
print(fruits)
print(fruits.pop())
print(fruits)

# Using Lists as Stacks
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
print(stack.pop())
print(stack.pop())
print(stack)

# Using Lists as Queue
# using collections.deque
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())
print(queue)

# List Comprehensions
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

# equivalent
squares = list(map(lambda x: x**2, range(10)))
print(squares)

# equivalent
squares = [x**2 for x in range(10)]
print(squares)

lists = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(lists)

#####
vec = [-4, -2, 0, 2, 4]
# create new list
print([x*2 for x in vec])
# filter
print([x for x in vec if x>=0])
# apply a function to all elmements
print([abs(x) for x in vec])
print([(x, x**2) for x in vec])

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([x.strip() for x in freshfruit])

# flatten
vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for ele in vec for num in ele])

# complex expressions and nested functions
from math import pi
print([str(round(pi, i)) for i in range(1, 6)])

# Nested List Comprehensions
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print(matrix)
# transpose rows and columns
print([[row[i] for row in matrix] for i in range(4)])
print(list(zip(*matrix)))

# del
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[2:4]
print(a)
del a[:]
print(a)

# Tuples and Sequences
t = 12345, 54321, 'hello!'
print(t[0])
print(t)
u = t, (1, 2, 3, 4, 5)
print(u)
v = ([1, 2, 3], [3, 2, 1])
print(v)
empty = ()
print(empty)
singleton = "hello",
print(singleton)
print(len(singleton))
t = 12345, 54321, 'hello!'
x,y,z = t
print(x)
print(y)
print(z)

# Sets
print("==== Sets ====")
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket)
print('orange1' in basket)
a = set('abracadabra')
b = set('alacazam')
print(a) # unique letters in a
print(b) # unique letters in b
print(a - b) # letters in a, but not in b
print(a | b) # letters in a or b or both
print(a & b) # letters in both a & b
print(a ^ b) # letters in a or b, not both
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

# Dictionaries
print("=== Dictionaries ===")
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])
del tel['sape']
print(tel)
print(list(tel))
print(list(tel.values()))
print('jack' in tel)
tel1 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(tel1)
tel2=dict(sape=4139, guido=4127, jack=4098)
print(tel2)

tel3 = {x: x**2 for x in (2, 4, 6)}
print(tel3)

### Looping Techniques
print("=== Looping Techniques ===")
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k,v in knights.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q,a in zip(questions, answers):
    print("What is your {0}?, its {1}".format(q,a))

for i in reversed(range(1, 10, 2)):
    print(i)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

# comparations
print ((1, 2, 3) < (1, 2, 4))
print ([1, 2, 3] < [1, 1, 5])