# defaultdict
from collections import defaultdict

colors = (
    ('태희', '노랑'),
    ('지훈', '파랑'),
    ('별이', '초록'),
    ('지훈', '검정'),
    ('태희', '빨강'),
    ('샛별', '실버'),
)

favorite_colors = defaultdict(list)

for name, color in colors:
    favorite_colors[name].append(color)

print(favorite_colors)
# 결과: defaultdict(<class 'list'>, {'태희': ['노랑', '빨강'], '지훈': ['파랑', '검정'], '별이': ['초록'], '샛별': ['실버']})

some_dict = {}
#some_dict['colors']['favorite'] = '노랑'
# 결과: KeyError: 'colors'

import collections
import json
tree = lambda: collections.defaultdict(tree)
some_defaultdict = tree()
some_defaultdict['color']['favorite'] = '노랑'
print(some_defaultdict)
# 결과: defaultdict(<function <lambda> at 0x1049ec040>, {'color': defaultdict(<function <lambda> at 0x1049ec040>, {'favorite': '노랑'})})
print(json.dumps(some_defaultdict, ensure_ascii=False))
# 결과: {"color": {"favorite": "노랑"}}

# OrderedDict
color_value = {'빨강': 198, '녹색': 170, '파랑': 160}
for key, value in color_value.items():
    print(key, value)
'''결과 - 차이가 없음 ㅡ.ㅡ;
빨강 198
녹색 170
파랑 160
'''
from collections import OrderedDict

ordered_colors = OrderedDict([("빨강", 198), ("녹색", 170), ("파랑", 160)])
for key, value in ordered_colors.items():
    print(key, value)
'''결과
빨강 198
녹색 170
파랑 160
'''

# counter
from collections import Counter
user_colors = (
    ('태희', '노랑'),
    ('지훈', '파랑'),
    ('별이', '초록'),
    ('지훈', '검정'),
    ('태희', '빨강'),
    ('샛별', '실버'),
)

favs = Counter(name for name, color in user_colors)
print(favs)
# 결과: Counter({'태희': 2, '지훈': 2, '별이': 1, '샛별': 1})

# deque(double ended queue)
from collections import deque
d = deque()
d.append('1')
d.append('2')
d.append('3')

print(len(d))
# 결과: 3
print(d[0])
# 결과: 1
print(d[-1])
# 결과: 3

d = deque([i for i in range(5)])
# deque([0, 1, 2, 3, 4])
print(len(d))
# 결과: 5
print(d.popleft())
# 결과: 0
print(d.pop())
# 결과: 4
print(d)
# 결과: deque([1, 2, 3])

d = deque([i for i in range(3)], maxlen=5)
print(d)
# 결과: deque([0, 1, 2], maxlen=5)
d.extend([3, 4, 5, 6])
print(d)
# 결과: deque([2, 3, 4, 5, 6], maxlen=5)
d.extendleft([1])
print(d)
# 결과: deque([1, 2, 3, 4, 5], maxlen=5)

# namedtuple
from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name='perry', age=31, type='cat')

print(perry)
# 결과: Animal(name='perry', age=31, type='cat')
print(perry.name)
# 결과: perry

# usable index
print(perry[0])
# 결과: perry

# dictionary
print(perry._asdict())
# 결과: {'name': 'perry', 'age': 31, 'type': 'cat'}

# tuple is immutable list.
# can't reassign
#>> perry.age = 42
'''결과
Traceback (most recent call last):
  File "/Users/kises/workspace/interpy/collections.py", line 115, in <module>
    perry.age = 42
AttributeError: can't set attribute
'''

# enum.Enum
from enum import Enum

class Species(Enum):
    cat = 1,
    dog = 2
    horse = 3
    aardvark = 4
    butterfly = 5
    owl = 6
    platypus = 7
    dragon = 8
    unicorn = 9
    kitten = 1,
    puppy = 2

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="Perry", age=31, type=Species.cat)
dragon = Animal(name="Drogon", age=4, type=Species.dragon)
tom = Animal(name="Tom", age=75, type=Species.cat)
charlie = Animal(name="Charlie", age=2, type=Species.kitten)

print(charlie.type == tom.type)
# 결과: True
print(charlie.type)
# 결과: Species.cat

print(Species['cat'])
print(Species.cat)
print(Species(1))
# 결과: Species.cat

'''index value 사용시 주의
class Species(Enum):
    cat = 1,
    dog = 2,
    horse = 3

print(Species(1))
# 결과: ValueError: 1 is not a valid Species

콤마까지 포함한 것으로 인식
class Species(Enum):
    cat = (1,)
    dog = (2,)
    horse = 3

콤마 제거할 것!!!
'''