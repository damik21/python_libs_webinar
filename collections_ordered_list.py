import collections

dict = {}
dict['a'] = 'A'
dict['b'] = 'B'
dict['c'] = 'C'

dict_1 = {}
dict_1['c'] = 'C'
dict_1['a'] = 'A'
dict_1['b'] = 'B'

print(dict==dict_1)
for key, value in dict.items():
    print(f'{key}:{value}')


o_dict = collections.OrderedDict()
o_dict['a'] = 'A'
o_dict['b'] = 'B'
o_dict['c'] = 'C'

o_dict_1 = collections.OrderedDict()
o_dict_1['c'] = 'C'
o_dict_1['a'] = 'A'
o_dict_1['b'] = 'B'

for key, value in o_dict_1.items():
    print(f'{key}:{value}')

o_dict_1.move_to_end('a', last=False)


for key, value in o_dict_1.items():
    print(f'{key}:{value}')

