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