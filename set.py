some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = []

for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)
# 결과: ['b', 'n']

dupl = set(some_list)
print(dupl)
# 결과: {'c', 'a', 'n', 'd', 'm', 'b'}

dupl_set = set([x for x in some_list if some_list.count(x) > 1])
print(dupl_set)
# 결과: {'n', 'b'}

valid = set(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])
print(input_set.intersection(valid))
# 결과: {'red'}

print(input_set.difference(valid))
# 결과: {'brown'}

a_set = {'red', 'blue', 'green'}
print(type(a_set))
# 결과: <class 'set'>