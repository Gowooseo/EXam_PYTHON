#-----------------------------------
#리스트-[[값,값],[값,값],[값,값]]
a=[[10,20],
   [30,40],
   [50,60]]

#import
# import 파일명( 라이브러리)
# ex import calendar
#   calendar.prmonth(함수이름)(2017,8) => 2017년 8월 달력 출력
#from
#앞의 예제를 from을 써서 간단하게 나타낼수 있다.
# from calendar import prmonth(아니면 *를 써도 됨)
# prmonth(2017,8)

# 반복문으로 2차원 리스트 출력
b=[[10,20],[30,40],[50,60]]
for x,y in b:
    print(x,y)

# 이 방식은 2차원 리스트의 가로크기가 크지 않을때 유효하다..

# 그렇다면 for 반복문을 두번 사용해 보자.
b1=[[10,20],[30,40],[50,60]]

for i in b1:
    for j in i:
        print(j,end=' ')
    print()

b2=[[10,20],[30,40],[50,60]]

for i in range(len(b2)):
    for j in range(len(b2[i])):
        print(b2[i][j],end=' ')
    print()

# 23.2.4 while 반복문 사용
b3=[[10,20],[30,40],[50,60]]
i=0
while i<len(a):
    x,y=a[i]
print(x,y)
i+=1
# 리스트에 인덱스를 지정해 값을 꺼내 올떄는 변수 두개를 지정해 주자
# x,y=a[i]
# 다끝났으면 i=i+1 인덱스를 1 증가 시켜 준다.


#23.2.5 while 반복문 두번 사용하기
a4=[[10,20],[30,40],[50,60]]
i=0
while i <len(a4):
    j=0
    while j <len(a4[i]):
        print(a4[i][j],end=' ')
        j+=1
    print()
    i+=1 # while 안쪽에서 이걸 반복하면 오류가 남


# 23.3 반복문으로 리스트 만들기
# for 반복문을 사용하여 2차원 리스트 만들기
# k=[]
# for k in range(3):
#     line=[]
#     for l in range(2):
#         line.append(0)
#     k.append(line)
#
# print(k)


# 23.3.3 리스트 표현식으로 2차원 리스트
# a=[[0 for j in range(2)] for i in range(3)]
# [[0,0],[0,0],[0,0]]

#23.3.4 톱니형 리스트 만들기

r1=[3,1,3,2,5]
r2=[]

for i in r1:
    line=[]
    for j in range(i):
        line.append(0)
    r2.append(line)

print(r2)

# 위에 것을 리스트 표현식 화
r2=[[0]*i for i in [3,1,3,2,5]]

