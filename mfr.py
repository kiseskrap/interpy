#map, filter, reduce
from functools import reduce

items = [1, 2, 3, 4, 5]
squared = []
for i in items:
  squared.append(i**2)
print(squared)
'''결과
[1, 4, 9, 16, 25]
'''

squared2 = map(lambda x: x ** 2, items)
print(list(squared2))
'''결과
[1, 4, 9, 16, 25]
'''

for i in squared2:
  print(i)
'''결과
1
4
9
16
25
'''

print(*squared2)
'''결과
1 4 9 16 25
'''

def multiply(x):
  return x * x

def add(x):
  return x + x

funcs = [multiply, add]
for i in range(5):
  value = map(lambda x: x(i), funcs)
  print(*value)
'''결과
0 0
1 2
4 4
9 6
16 8
'''

number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

# product = (lambda x,y: x * y)(2, 3)
product = reduce(lambda x,y: x * y, [1, 2, 3, 4])
print(product)
# 결과: 24

