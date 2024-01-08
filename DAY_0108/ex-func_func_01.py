#----------------------------------------
# 함수 안에 함수 정의 및 호출
#----------------------------------------
def print_hello():
    hello='hello~'

    def print_message():
        msg=hello+" ^^ "
        print(hello)

    print_message()
# 함수 호출

print_hello()


#nonlocal

def a():
    x=10   # 함수 a의 지역변수 x
    def b():
        nonlocal x  # 가장 가까운 '바깥'함수에서 변수 x를 찾음
        x=20 # 함수  b의 지역변수 x
    #호출
    b()
    print(x)
a()


# 함수 호출--------------------------
# a() ====> #원래는 10이 추출됨


#클로저 함수
def foo():
    x=10
    def test():
        return x

    return test()

# 함수 호출
x=foo()
print(x(),x)