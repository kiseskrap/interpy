'''예시
for counter, value in enumerate(some_list):
    print(counter, value)
'''

my_list = ['사과', '바나나', '포도', '배']
for c, value in enumerate(my_list):
    print(c, value)
'''결과
0 사과
1 바나나
2 포도
3 배
'''

# startIndex = 1 로 설정
for c, value in enumerate(my_list, 1):
    print(c, value)
'''결과
1 사과
2 바나나
3 포도
4 배
'''

counter_list = list(enumerate(my_list, 1))
print(counter_list)
# 결과: [(1, '사과'), (2, '바나나'), (3, '포도'), (4, '배')]