#-------------------------------------------------------------------
# 모듈(Module): 특정 목적의 변수 , 함수, 클래스를 하나의 파일에 담은 것
# -예: 수학 관련 변수,함수,클래스 => math.py
#       파이썬 기본 제공 변수, 함수, 클래스 => builtin.py
#  - 사용법: import 모듈명
# - 모듈의 기능 사용법: 모듈명, 변수명
#                    모듈명, 함수명()
#-------------------------------------------------------------------
# 사용하고 싶은 변수, 함수, 클래스가 있는 모듈 포함
import random  # 임의의 수를 추출 해주는 변수,함수,클래스 있는 모듈
import math    # 수학 관련 변수,함수,클래스가 있는 모듈

# 모듈 안에 있는 변수,함수,클래스 사용
print(math.pi)

print(math.factorial(5))

#0.0 <=~ <1.0 사이의 실수 추출=> random()함수
for cnt in range(10):
    print(int(random.random()*10))
#1<=~<=10 정수를 추출
for cnt in range(10):
    print(int(random.random()*10)+1)

# a<= ~ <= 사이의 임의의 정수 추출 => randint()함수
for cnt in range(6):
    print(random.randint(1,45),end=' ')
myLotto=[]
END_POINT=11

while True:
    if len(myLotto)==END_POINT:
        break
    num=random.randint(1,10)
    if num not in myLotto:
        myLotto.append(num)


print(f'myLotto => {myLotto}')
