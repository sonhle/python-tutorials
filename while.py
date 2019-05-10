words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))


# insert
for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)

print(words)


# range
for i in range(5):
    print(i)

for w in range(0, 21, 5):
    print(w)

# range is not a list
lists = range(5, 10)
print(lists)
print(list(lists))
print(list(range(2,2)))

# break
# for else
for n in range(2, 10):
    for x in range(2, n):
        if x % n == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')

# continue
# for else
for n in range(2, 10):
    if n % 2 == 0:
        print("Found an even number", 2)
        continue
    print("Found a number", n)


# pass - wait for or breakpoint
while True:
    pass

print('OK')