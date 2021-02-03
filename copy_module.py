import copy

a = ['a', 'b', 'c']
b = ['d', 'e', 'f']
c = [a, b]

d = copy.deepcopy(c)
print(c)
print(d)
a.append('z')
print(a)
print(c)
print(d)

