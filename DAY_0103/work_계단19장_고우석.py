#-----
#19.1 중첩 루프
# 반복문 안에 반복문이 들어가는 것을 다중 루프, 중첩 루프 라고 한다.
#형식
        # for i in range(횟수):
            #for j in range(횟수):
                #가로 처리 코드
            #세로 처리 코드

for i in range(5):
    for j in range(5):
        print('j:',j,sep='',end=' ')
    print('i:',i,'\\n',sep='')

# 19.2 사각형으로 별 출력하기
for i in range(5):
    for j in range(5):
        print('*',end='')
    print()

#19.2.1 사각형 모양 바꾸기
for i in range(3):
    for j in range(7):
        print('*',end='')
    print()
#19.3 계단식으로 별 출력하기
for j in range(5):
    for i in range(5):
        if i<=j:
            print('*',end='')
    print()

#----------------------------- 대각선 출력
for i in range(5):
    for j in range(5):
        if j==i:
            print('*',end='')
        else:
            print(' ',end='')
    print()

# 19.5 연습문제:역삼각형 모양으로 별 출력하기

for i in range(5):
    for j in range(5):
        if j>=i:
            print('*',end='')
        else:
            print(' ',end='')
    print()


# 19.6 심사문제: 산 모양으로 별 출력하기
# 1)표준 입력으로 삼각형의 높이 입력
height=int(input())

# 2)문제 만들기
for i in range(1,height+1):
    sss=2*i-1
    print(' '*(height-i)+'*'*sss,sep=' ')


