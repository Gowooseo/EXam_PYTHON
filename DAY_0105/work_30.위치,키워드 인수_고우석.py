#-----30.1 위치인수 만들기
#
# def print_numbers(a,b,c):
#     print(a)
#     print(b)
#     print(c)
#
# print_numbers(10,20,30)
#
# # 30.1.2 언패킹 사용
# x=[10,20,30]
# print_numbers(*x)
# print_numbers(*[10,20,30])
# # print_numbers(*[10,20])  #error
#
# #30.1.3 가변 인수 만들기
# def print_num(*args):
#     for arg in args:
#         print(arg)
#
# print_num(10)
# print_num(10,20,30,40)
#
# x=[10]
# print_numbers(*x)
#
# y=[10,20,30,40]
# print_numbers(*y)


#30.2 키워드 함수
# 함수(키워드=값)
# def personal_info(name,age,address)
#     print('이름:', name)
#     print('나이:',age)
#     print('주소:',address)
#
# personal_info(name='홍길동',age=30,address='서울시 용산구 이촌동')

# 30.3 키워드 인수와 딕셔너리 언패킹 사용
#함수(**딕셔너리)
# x={'name':'홍길동','age':30,'address':'서울시 용산구 이촌동'}
# personal_info(**x)

#30.3.2  키워드 인수를 사용하는 가변 인수 함수 만들기
# def 함수이름(**매개변수):
#     코드
#값 여러개를 받아 매개변수 이름과 값을 각 줄에 출력하는 함수를 만들어보자.
def personal(**kwargs):
    for kw,args in kwargs.items():
        print(kw,':',args,sep='')

personal(name='홍길동')
personal(name='홍길동',age=30,address='서울시 용산구 이촌동')

x1={'name':'홍길동'}
personal(**x1)
y={'name':'홍길동','age':30,'address':'서울시 용산구 이촌동'}
personal(**y)
#30.4 매개변수에 초깃값 지정

# def 함수이름(매개변수=값)
def ex(name,age,address='비공개'):
    print('이름',name)
    print('나이', age)
    print('주소', address)

ex('홍길동',30)
print(ex('홍길동',30))

# 30.6
# 가장 높은 점수를 구하는 함수 만들기
korean,english,mathmatics,science=100,86,81,91
def get_max_score(*args):
    return max(args)



max_score=get_max_score(korean,english,mathmatics,science)
print('높은 점수:',max_score)

max_score=get_max_score(english,science)
print('높은 점수:',max_score)


# 30.7.심사문제:
# 가장 낮은 점수,높은 점수와 평균 점수를 구하는 함수

# korean,english,mathmatics,science=map(int,input().split())
# def get_min_max_score(*args):
#     return max(args),min(args)
# def get_average(**kwargs):
#     return sum(kwargs.values()),len(kwargs)


