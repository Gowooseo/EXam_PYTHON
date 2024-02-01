#for 변수 in range(횟수):

#16.2.2 증가폭 사용하기
for i in range(0,10,2):
    print('Hello,world!',i)

# 16.2.3 숫자를 감소시키기
for i in range(10,0,-1):
    print('Hello,world!',i)

#16.2.4 입력한 횟수대로 반복하기
count=int(input('반복할 횟수를 입력하세요: '))
for i in range(count):
    print('Hello world!',i)
#16.3 시퀀스 객체로 반복하기
a=[10,20,30,40,50]
for i in a:
    print(i)

a=(10,20,30,40,50)
for i in a:
    print(i)

for letter in 'Python':
    print(letter,end=' ')

# 16.5 연습문제:리스트의 요소에 10을 곱해서 출력하기
x=[49,-17,5,102,8,62,21]
for i in x:
    print(i*10,' ')

#16.6 심사문제 구구단 출력하기

for num in range(10):
    for dan in range(2,10):
        if num:
            print(f'{dan}*{num}={dan*num:^3}',end=' ' if dan!=9 else '\n')
        else:
            print(f'{dan:-^7}단',end=' ' if dan!=9 else '\n')