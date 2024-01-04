#-----------------------------
#1.while으로 hello world 100번 반복하기.
i=0
while i<100:
    print('hello world')
    i+=1
print()

# for i1 in range(100):
#     print('hello world')

# 17.1.1 초깃값을 1부터 시작하기(업카운팅)
i=1
while i<=100:
    print('hello world',i)
    i+=1

#17.1.2 초깃값을 감소시키기(다운카운팅)
i=100
while i>0:
    print('hello world',i)
    i-=1
# 17.1.3 입력한 횟수대로 반복하기

count= int(input('반복할 횟수를 입력하세요: '))

i=0
while i<count:
    print('hello world',i)
    i+=1

#17.2 반복횟수가 정해지지 않은 경우
#import random 모듈: random 모듈을 가져옴
import random
random.random()

print(random.randint(1,6))

#while 반복문에 randint 사용하기
import random
i=0
while i!=3:
    i=random.randint(1,6)
    print(i)

#17.5 연습문제:변수 두개를 다르게 반복 하기
i=2
j=5

while i<=32 or j>=1:
    print(i,j)
    i*=2
    j-=1

# 17.6 심사문제 :교통카드 잔액 출력하기

money=int(input('금액을 입력하세요.'))
while money>0:
    print(money)
    money=money-1350

