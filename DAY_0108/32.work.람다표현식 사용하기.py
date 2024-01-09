#--------------------------
# 32.1 람다 표현식으로 함수 만들기

def plus_ten(n):
    return n+10

print(plus_ten(1))

# 이름없는 함수 람다 표현식 만들기
plus_ten=lambda n:n+10
print(plus_ten(1))

print((lambda x:x+10)(1))

# 람다 안에서는 변수를 만들 수 없다.
# (lambda x:y=10;x+y)(1)


#32.1.3 람다를 사용하는 이유
# 람다의 사용이유는 map함수를 사용하여 보다 쉽게 인수로 나타내기 위함이다.
def plus_ten(x):
    return x+10
list(map(plus_ten,[1,2,3]))

list(map(lambda x:x+10,[1,2,3]))
print(list(map(lambda x:x+10,[1,2,3])))
# 람다의 조건식
a=[1,2,3,4,5,6,7,8,9,10]
list(map(lambda x:str(x) if x/3==0 else x,a))

# list(map(lambda x:str(x) if x%3 == 0,a))
# if만 사용하면 문법 에러 발생

#32.2.3 filter 사용하기
def f(x):
    return x>5 and x<10
a=[8,3,2,10,15,7,1,9,0,11]
list(filter(f,a))

#32.2.4 reduce 사용하기
def f(x,y):
    return x+y
a=[1,2,3,4,5]
from functools import reduce
reduce(f,a)

#람다로 만들기
a=[1,2,3,4,5]
from functools import reduce
reduce(lambda x,y:x+y,a)
print(reduce(lambda x,y:x+y,a))


