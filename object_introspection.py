# dir

my_list = [1, 2, 3]
print(dir(my_list))

''' 결과
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
'''

# type
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

# id
name = 'kises'
print(id(name))
# 결과: 4310190512


# inspect module

import inspect
print(inspect.getmembers(str))
''' 결과
[('__add__', <slot wrapper '__add__' of 'str' objects>), ('__class__', <class 'type'>), ('__contains__', \
<slot wrapper '__contains__' of 'str' objects>), ('__delattr__', <slot wrapper '__delattr__' of 'object' \
objects>), ('__dir__', <method '__dir__' of 'object' objects>), ('__doc__', "str(object='') -> \
str\nstr(bytes_or_buffer[, encoding[, errors]]) -> str\n\nCreate a new string object from the \
given object. If encoding or\nerrors is specified, then the object must expose a data buffer\nthat will be decoded \
using the given encoding and error handler.\nOtherwise, returns the result of object.__str__() (if defined)\nor \
repr(object).\nencoding defaults to sys.getdefaultencoding().\nerrors defaults to 'strict'."), \
('__eq__', <slot wrapper '__eq__' of 'str' objects>), ('__format__', <method '__format__' of 'str' objects>), \
('__ge__', <slot wrapper '__ge__' of 'str' objects>), ('__getattribute__', <slot wrapper '__getattribute__' \
of 'str' objects>), ('__getitem__', <slot wrapper '__getitem__' of 'str' objects>), ('__getnewargs__', \
<method '__getnewargs__' of 'str' objects>), ('__gt__', <slot wrapper '__gt__' of 'str' objects>), \
('__hash__', <slot wrapper '__hash__' of 'str' objects>), ('__init__', <slot wrapper '__init__' of \
'object' objects>), ('__init_subclass__', <built-in method __init_subclass__ of type object at 0x105444868>), \
('__iter__', <slot wrapper '__iter__' of 'str' objects>), ('__le__', <slot wrapper '__le__' of 'str' objects>), \
('__len__', <slot wrapper '__len__' of 'str' objects>), ('__lt__', <slot wrapper '__lt__' of 'str' objects>), \
('__mod__', <slot wrapper '__mod__' of 'str' objects>), ('__mul__', <slot wrapper '__mul__' of 'str' objects>), \
('__ne__', <slot wrapper '__ne__' of 'str' objects>), ('__new__', <built-in method __new__ of type object at \
0x105444868>), ('__reduce__', <method '__reduce__' of 'object' objects>), ('__reduce_ex__', <method '__reduce_ex__' \
of 'object' objects>), ('__repr__', <slot wrapper '__repr__' of 'str' objects>), ('__rmod__', \
<slot wrapper '__rmod__' of 'str' objects>), ('__rmul__', <slot wrapper '__rmul__' of 'str' objects>), ('__setattr__', <slot wrapper '__setattr__' of 'object' objects>), ('__sizeof__', <method '__sizeof__' of 'str' objects>), ('__str__', <slot wrapper '__str__' of 'str' objects>), ('__subclasshook__', <built-in method __subclasshook__ of type object at 0x105444868>), ('capitalize', <method 'capitalize' of 'str' objects>), ('casefold', <method 'casefold' of 'str' objects>), ('center', <method 'center' of 'str' objects>), ('count', <method 'count' of 'str' objects>), ('encode', <method 'encode' of 'str' objects>), ('endswith', <method 'endswith' of 'str' objects>), ('expandtabs', <method 'expandtabs' of 'str' objects>), ('find', <method 'find' of 'str' objects>), ('format', <method 'format' of 'str' objects>), ('format_map', <method 'format_map' of 'str' objects>), ('index', <method 'index' of 'str' objects>), ('isalnum', <method 'isalnum' of 'str' objects>), ('isalpha', <method 'isalpha' of 'str' objects>), ('isascii', <method 'isascii' of 'str' objects>), ('isdecimal', <method 'isdecimal' of 'str' objects>), ('isdigit', <method 'isdigit' of 'str' objects>), ('isidentifier', <method 'isidentifier' of 'str' objects>), ('islower', <method 'islower' of 'str' objects>), ('isnumeric', <method 'isnumeric' of 'str' objects>), ('isprintable', <method 'isprintable' of 'str' objects>), ('isspace', <method 'isspace' of 'str' objects>), ('istitle', <method 'istitle' of 'str' objects>), ('isupper', <method 'isupper' of 'str' objects>), ('join', <method 'join' of 'str' objects>), ('ljust', <method 'ljust' of 'str' objects>), ('lower', <method 'lower' of 'str' objects>), ('lstrip', <method 'lstrip' of 'str' objects>), ('maketrans', <built-in method maketrans of type object at 0x105444868>), ('partition', <method 'partition' of 'str' objects>), ('removeprefix', <method 'removeprefix' of 'str' objects>), ('removesuffix', <method 'removesuffix' of 'str' objects>), ('replace', <method 'replace' of 'str' objects>), ('rfind', <method 'rfind' of 'str' objects>), ('rindex', <method 'rindex' of 'str' objects>), ('rjust', <method 'rjust' of 'str' objects>), ('rpartition', <method 'rpartition' of 'str' objects>), ('rsplit', <method 'rsplit' of 'str' objects>), ('rstrip', <method 'rstrip' of 'str' objects>), ('split', <method 'split' of 'str' objects>), ('splitlines', <method 'splitlines' of 'str' objects>), ('startswith', <method 'startswith' of 'str' objects>), ('strip', <method 'strip' of 'str' objects>), ('swapcase', <method 'swapcase' of 'str' objects>), ('title', <method 'title' of 'str' objects>), ('translate', <method 'translate' of 'str' objects>), ('upper', <method 'upper' of 'str' objects>), ('zfill', <method 'zfill' of 'str' objects>)]
'''