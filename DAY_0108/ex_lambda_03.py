#----------------------------------------------
# filter(함수명,반복가능객체)
#- 조건에 맞는 데이터만 반환
#----------------------------------------------
import random             # random.py 파일에 모든 변수,함수,클래스 가져오기
from random import randint,random  # random.py 파일에서 randint 함수만 가져오기
from functools import reduce         #funtools.py 파일에서 reduce 함수만 가져오기




#예) 5초과 10미만 데이터만 추출
a=[8,3,2,10,15,7,1,9,1,0,11]

def check(data):
    return data>5 and data<10
a=list(filter(check,a))
print(a)

randint(1,10)
random()

def f(x,y):
    return x+y
print(reduce(f,a))

print(reduce(lambda x,y:x+y,a) )


