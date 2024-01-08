# #--------------------------
# #29.1 hello world! 출력 함수 만들기
# def hello():
#     print('Hello,world!')
# #29.1.2 함수 호출하기
# hello()
#
# # 29.1.3 소스 파일에서 함수를 만들고 호출하기
# def hello():
#     print('Hello,world!')
# hello()
# # 함수를 만들떄는 함수를 먼저 호출해서는 안된다.
# hello()
#
# def hello():
#     print('Hello,world!')
#
#
# # 29.2 덧셈 함수 만들기
# def add(a,b):
#     print(a+b)
#
# #29.3 함수의 결과를 반환하기
#
# def add(a,b):
#     return a+b

#29.4 함수에서 값을 여러 개 반환하기
def add_sub(a,b):
    return a+b,a-b

x=add_sub(10,20)
print(x)

#29.5 함수의 호출과정 알아보기

def mul(a,b):
    c=a*b
    return c

def add(a,b):
    c=a+b
    print(c)
    d=mul(a,b)
    print(d)

x=10
y=20
add(x,y)


# 29.7 연습 문제: 몫과 나머지를 구하는 함수 만들기

x=10
y=3

def get_quotient_remainder(a,b):
    return a//b,a%b
quotient,remainder=get_quotient_remainder(x,y)
print('몫:{0},나머지:{1}'.format(quotient,remainder))

# 29.8 심사문제: 사칙연산 함수 만들기
def fourCal(x,y):
    return f'덧셈:{x+y},뺄셈:{x-y},곱셈:{x*y},나눗셈:{x/y}' if y>0 else '0으로 나눌수 없습니다.'

print(fourCal(10,0))


