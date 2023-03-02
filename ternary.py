# ternary
# condition_is_true if condition_true else condition_is_false
is_fat = True
state = "fat" if is_fat else "not fat"
print(state)
# 결과: fat

# tuple
# (if_test_is_false, if_test_is_true)[test]
fat = True
fitness = ("skinny", "fat")[fat]
print("Ali is", fitness)
# 결과: Ali is fat

condition = True
print(2 if condition else 1/0)
# 결과: 2
print((1/0, 2)[condition])
'''결과
ZeroDivisionError: division by zero

# condition 값은 True 인데, false 요소에 있는 1/0 까지 (굳이) 검사를 진행했음
# 튜플 삼항연산자의 경우, 조건에 상관없이 각 요소를 모두 체크하므로 그 사용을 피하는게 좋다
'''

