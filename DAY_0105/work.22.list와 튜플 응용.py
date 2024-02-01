#-----------------------
# 22.1.2 리스트에 요소 추가
# append메서드 사용
a=[10,20,30]
a.append(500)
print(len(a),a)

# extend의 활용법, 여러개 요소 추가

a.extend([150,250])
print(a,len(a))
# 리스트로 묶여 있던 150,250이 요소별로 삽입됨

#insert(인덱스,요소)
# 원하는 인덱스에 넣을 수도 있음, 이경우 index(인덱스,요소) 메서드를 사용함, 단 이때 원래 있던 값은 오른쪽으로 밀려간다.

a1=[10,20,30]
a1.insert(2,40)
print(a1)

#22.1.6 리스트에서 요소 삭제하기
a1.pop()
#가장 마지막 요소가 삭제 된다.

# 22.1.8 리스트에서 특정값 찾아 삭제 remove(값)
a1.remove(20)

#값이 여러개일경우 처음 찾은 값을 삭제한다.

# 22.1.9 리스트에서 특정 값의 인덱스 구하기
b=[10,20,30,40,50]
b.index(50)
print(b.index(50))

#22.1.10 특정 값의 개수 구하기
# count(값)
kp=[10,20,30,45,10,20,30,30]
print(kp.count(20))

#리스트 순서 뒤집기
#reverse()
kp.reverse()
print(kp)

# 리스트 요소 정렬하기
kj=[10,20,30,15,20,40]
kj.sort()
print(kj)
kj.sort(reverse=True) # 내림차순 정렬
print(kj)
# kj.sorted()
print(kj)

#리스트의 모든 요소 삭제 clear()

#리스트의 슬라이스로 조작
g=[10,20,30]
g[len(g):]=[500]
# 마지막 인덱스보다 1이 큰 곳에 500이라는 값을 집어 넣는다. =g.append(500)

#a[len(a):]=a.extend([500,600])

#22.3 for 반복문으로 리스트 요소 전부 출력
tsk=[38,21,53,62,19]

for i in tsk:
    print(i,end=' ')


#### 중요! 인덱스와 요소 함께 출력하기! for 인덱스,요소 enumerate(리스트이름)

for index,value in enumerate(tsk):
    print(f'인덱스번호 {index}',value)

# 파이썬에서만 되는 것
# for 인덱스,요소 in enumerate(리스트,start=시작할 숫자):
# 인덱스를 1부터 시작할 경우
for index,value in enumerate(tsk,start=1):
    print(index,value)

# while 반복문으로 요소 출력하기
tsk=[38,21,53,62,19]
i=0
while i<len(tsk):
    print(tsk[i])
    i+=1


#리스트 표현식 사용
a2=[i for i in range(10)]
b2=[i for i in range(10)]
print(a2,b2)

# 리스트 표현식에서 if 조건문 사용 저장할 변수=[i for i in range(x) if 조건]
a3=[i for i in range(10) if i%2==0]
print(a3)

gugudan=[i*j for j in range(2,10) for i in range(1,10)]
print(gugudan)

# 22.6 리스트에 map 사용하기

# list(map(함수,리스트))
# tuple(map(함수,튜플))

hhh=[1.3,2.7,3.8,4.5]
for i in range(len(hhh)):
    hhh[i]=int(hhh[i])
print(hhh)
hhh=list(map(int,hhh))

#연습문제:리스트에서 특정요소만 뽑기
#길이가 1인 요소만 뽑기
n=['a','b','c','d','e','f','g','h','i']
m= [i for i in n if len(i)==1]

print(m)

# #20.10 심사문제:2의 거듭제곱 리스트 생성하기
# i1,i2=map(int,input().split())
# double=[k**2 for k in range(i1,i2+1)]
# del double[-2]
# del double[1]
# print(double)