lists = [1, 4, 9, 16, 25]
print(lists)
print(lists[1])
print(lists[-1])
print(lists[:3])
print(lists[2:])
print(lists[-2])

# concat
lists = lists + [36, 49, 64, 81, 100]
print(lists)

# mutable
lists[2] = 'test'
print(lists)

# lists & nested & referenced
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
numbers = [1, 2, 3, 4]
x = [letters, numbers]
print(x)

# nested access
print(x[0][:2])
#repace values
letters[2:5] = ['C', 'D', 'E']
print(letters)
print(x)
# remove
letters[2:5] = []
print(letters)
# clear
letters[:] = []
print(letters)
print(x)