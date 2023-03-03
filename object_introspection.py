# dir

my_list = [1, 2, 3]
print(dir(my_list))

''' 결과
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
'''

# type, id
print(type(''))
# 결과: <class 'str'>
print(type([]))
# 결과: <class 'list'>
print(type({}))
# 결과: <class 'dict'>
print(type(bool))
# 결과: <class 'type'>
print(type(3))
# 결과: <class 'int'>

name = 'kises'
print(id(name))
# 결과: 4310190512

import inspect
print(inspect.getmembers(str))