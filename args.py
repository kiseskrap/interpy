def test_var_args(f_arg, *argv):
    print("첫 인자:", f_arg)
    for arg in argv:
        print("*argv 인자", arg)

test_var_args('야숩', 'python', '달걀', '테에스트')
'''결과
첫 인자: 야숩
*argv 인자 python
*argv 인자 달걀
*argv 인자 테에스트
'''

def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print("%s == %s" % (key, value))

greet_me(name="yasoob")
'''결과
name == yasoob
'''

def test_args_kwargs(arg1, arg2, arg3):
        print ("인자1:", arg1)
        print ("인자2:", arg2)
        print ("인자3:", arg3)

args = ("two", 3, 5)
test_args_kwargs(*args)
'''결과
인자1: two
인자2: 3
인자3: 5
'''

kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
test_args_kwargs(**kwargs)
'''결과
인자1: 5
인자2: two
인자3: 3
'''