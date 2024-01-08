#18.1.1 while에서 break로 반복문 끝내기
i=0
while True:
    print(i)
    i+=1
    if i==100:
        break

# 18.1.2 for에서 break로 반복문 끝내기
for i in range(10000):
    print(i)
    if i==100:
        break

#continue 사용
for i in range(100):
    if i%2==1:
        print(i)
        
# 18.2.2 while 에서 코드 실행 건너뛰기(홀수만 출력)
i=0
while i<100:
    i+=1
    if i%2==0:
        continue
    print()

# 18.3 입력한 횟수대로 반복하기

count=int(input('반복 횟수 입력:'))
t=0

while True:
    print(t)
    t+=1
    if t==count:
        break

# 18.3.1 입력한 숫자까지 홀수 출력
count1=int(input())

for j in range(count1+1):
    if j%2==0:
        continue
    print(j)
# 18.5 연습문제:3으로 끝나는 숫자만 출력
i1=0
while True:
    if i1 % 10!=3:
        i1+=1
        continue
    if i1>73:
        break
    print(i1,end=' ')
    i1+=1

# 18.6 심사문제: 두 수 사이의 숫자 중 3으로 끝나지 않는 숫자 출력하기
#num1,num2=map(int,input().split())
num1, num2 = 21 , 333
t=num1-1

while True:
    t+=1
    if str(t)[-1]=='3':
        if t == num2:
            break
        else:
            continue
    print(str(t),end=' ')

    if t>=num2:
       break



