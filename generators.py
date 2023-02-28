def generator_function():
    for i in range(5):
        yield i

for item in generator_function():
    print(item)

'''결과
0
1
2
3
4
'''

def fibon(n):
    a = b = 1
    for i in range(n):
        print('i: %s, a: %s, b: %s' % (i, a, b))
        yield a
        a, b = b, a+b

for x in fibon(10):
    print('x = a ------------------>', x)

'''결과
i: 0, a: 1, b: 1
x = a ------------------> 1
i: 1, a: 1, b: 2
x = a ------------------> 1
i: 2, a: 2, b: 3
x = a ------------------> 2
i: 3, a: 3, b: 5
x = a ------------------> 3
i: 4, a: 5, b: 8
x = a ------------------> 5
i: 5, a: 8, b: 13
x = a ------------------> 8
i: 6, a: 13, b: 21
x = a ------------------> 13
i: 7, a: 21, b: 34
x = a ------------------> 21
i: 8, a: 34, b: 55
x = a ------------------> 34
i: 9, a: 55, b: 89
x = a ------------------> 55
'''

def generator_function():
    for i in range(3):
        yield i

gen = generator_function()
print(next(gen))
# 결과: 0
print(next(gen))
# 결과: 1
print(next(gen))
# 결과: 2
#print(next(gen))
'''결과
Traceback (most recent call last):
  File "/Users/kises/workspace/interpy/generators.py", line 60, in <module>
    print(next(gen))
StopIteration
'''

my_string = "Kises"
# next(my_string)
# 에러: No overload variant of "next" matches argument type "str"mypy(error)
my_iter = iter(my_string)
print(next(my_iter))

