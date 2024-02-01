# 22.1.2 리스트에 요소 추가
# 1) append 메서드 사용
a=[10,20,30]
a.append(500)
print(a)
# 가장 오른쪽에 값이 삽입 된다.

# 22.1.3 리스트 안에 리스트 추가
a=[10,20,30]
a.append([500,600])
print(a)
print(len(a))

#22.1.4 리스트 확장
# append는 여러번 해야하므로 번거롭다.
#따라서 이번에는 extend 메서드를 사용한다.
a=[10,20,30]
a.extend([500,600])
print(a)
print(len(a))
# append와 extend의 차이점은 extend의 경우 시퀀스 값안의 요소 하나 하나를 분리해서 집어넣어 준다는 것이다.

# 22.1.5 리스트의 특정인덱스에 요소 추가하기
#append와 extend는 리스트 끝에 요소를 추가한다. 그렇다면 원하는 위치에 요소를 추가하는 방법은?
# insert(인덱스,요소)를 사용해 원하는 위치에 요소를 삽입할수 있다.
b=list(range(10,31,10))
b.insert(2,500)
print(b)
print(len(b))
# 이와 같이 인덱스 2의 위치에 500의 값이 삽입되었다. 그러나 원래 있던 30은 사라지지 않고 인덱스 3으로
# 자연스럽게 이동한다.

# 22.1.7 리스트에서 특정 인덱스 요소를 삭제
a=[10,20,30]
a.pop()
print(a)
# pop은 비워둘경우 마지막 요소를 삭제한다. 그렇다면 인덱스를 지정한다면 어떻게 되는가.
a.pop(1)
print(a)
#인덱스 1의 20이 pop으로 사라진 것을 확인할 수 있다.(del 을 사용해도 된다)
#22.1.8 리스트에서 특정 값을 찾아서 삭제하기
# 리스트에서 원하는 값을 찾아 삭제하기 위해서는 remove(값)라는 메서드가 필요하다.
c=[10,20,30]
c.remove(20)
print(c)
#이처럼 값20이 삭제 된 것을 볼수 있다.
c1=[10,20,30,20]
c1.remove(20)
print(c1)
#값이 중복될 경우 왼쪽에서 처음 나타난 값을 삭제하는 것을 볼 수 있었다.

# 22.1.9 리스트에서 특정 값의 인덱스 찾기
#index는 리스트에서 특정값의 인덱스를 구한다.
a=[10,20,30,15,20,40]
idx=a.index(20)
print(idx)
#20의 인덱스인 1이 나타남을 알 수 있다.(print 함수를 써야하지만)

# 22.1.10 특정 값의 개수 구하기
count1=[10,20,30,15,20,40]
count1.count(20)
print(count1.count(20))
# 22.1.11 리스트 요소 뒤집기

re=[10,20,30,15,20,40]
re.reverse()
# 요소를 그냥 거꾸로 한다.
#22.1.13 리스트의 모든 요소를 삭제하기
a=[10,20,30]
del a[:]
print(a)
# 처음부터 끝까지 전부 지우려면 [:]를 사용할 수 있다.

#22.1.14 리스트를 슬라이스로 조작하기
control=[10,20,30]
control[len(control):]=[500,600]
#len(a)는 인덱스 마지막 숫자보다 1큰 숫자다.따라서 이경우 [500,600]이 리스트의 마지막에 삽입될 것이다.
#22.2 리스트를 다른 변수에 할당
l1=[0,0,0,0,0]
l2=l1
print(l2 is l1)
#이들을 다른 리스트로 만들려면 copy 메서드로 복사해야 한다.
l1=[0,0,0,0,0]
l2=l1.copy()
print(l2 is l1)

#22.3.1 반복문으로 리스트의 요소를 모두 출력하기
a=[38,21,53,62,19]
for i in a:
    print(i)
#i안에 a의 값을 넣고 뽑아넣었다.
# 22.3.2 인덱스와 요소를 함께 출력하기
ald=[38,21,53,62,19]
#for 반복문으로 출력할떄 인덱스도 함꼐 출력하려면?=> enumerate() 메서드
for index,value in enumerate(ald):
    print(f'인덱스 번호={index},값{value}')

for index,value in enumerate(ald,1):
    print(f'인덱스 번호={index},값{value}')
# 이처럼 인덱스를 지정하여 enumerate를 사용해 볼수도 있다.

#22.3.3
# while 반복문은 아직 배우지 않아 견본만 쳐둔다
a=[38,21,53,62,19]
i=0
while i<len(a):
    print(a[i])
    i+=1
# 22.5 리스트 표현식 구하기
# 리스트 컴프리헨션
# [식 for 변수 in 리스트]
#list(식 for 변수 in 리스트)
g=[i for i in range(10)]
f=list(i for i in range(10))
print(f)
f1=[i+5 for i in range(10)]
print(f1)
# 다음과 같이 원래 값에다 5를 추가한 값을 가진 리스트가 생성 된다.

#if 조건 식도 넣어 볼 수 있다.(ex, 짝수 생성해서 5더하는 리스트)
f2=[i+5 for i in range(10) if i%2==0]
print(f2)

# 22.5.2 for 반복문 if 반복문 여러번 사용하기
# gs=[i*j for j in range(2,10) for i in range(1,10)]
# print(gs)
#봐도 모르겠어서 물어봐야 겠습니다.

#22.6 리스트에 map 사용하기
# mmp=[1.2,2.5,3.7,4.6]
# for i in range(len(i)):
#     mmp[i]=int(mmp[i])
#     # 이렇게 복잡한 반복문도
# mmp=[1.2,2.5,3.7,4.6]

#22.9 연습문제 :리스트에서 특정요소만 뽑아내기
# ag=['alpha','bravo','charlie','delta','echo','foxtrot','golf','hotel','india']
# bg= [i for i in a if len(i)==5]
#   들어오는 곳    반복문     조건

# 심사문제 :2의 거듭제곱 리스트 생성하기
i1,i2=map(int,input().split())
list1 = []
for a in range(i1,i2+1):
    list1.append(2**a)
print(list1)