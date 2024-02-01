# 딕셔너리의 조작

# 딕셔너리에 키-값-쌍 추가
# setdefault: 키-값-쌍 추가
# update: 키 값 수정, 키 없으면 키-값-쌍 추가

#25.1.2 딕셔너리에 키와 기본값 저장
x={'a':10,'b':20,'c':30,'d':40}
x.setdefault('e')
# 키에 e가 추가, 값은 none으로 입력 됨.
x.setdefault('f',60)
print(x)

# 25.2.3 딕셔너리 키 값 수정
x={'a':10,'b':20,'c':30,'d':40}
x.update(e=50,a=900,f=60)
print(x)

#update(반복 가능 객체)
y={1:'one',2:'two'}
y.update(zip([1,2],['one','two']))
print(y)
y.update([[2,'Two'],[4,'FOUR']])

# 21.1.4 딕셔너리에서 키-값 쌍 삭제

#pop(키) , 키와 값을 쌍으로 삭제, 그 값을 반환
#pop(키, 기본값) => 만약 키 값이 없으면 설정한 기본값만을 반환

#25.1.7 키의 값 가져오기 get(키,기본값)


#25.1.9 리스트와 튜플로 딕셔너리 만들기
# 1. keys=['a','b','c','d']와 같은 리스트를 준비(튜플도 됨)
# 2. dict.fromkeys(키리스트)에 딕셔너리를 넣는다. 이경우 키만 넣어, 값은 전부 none 값이 된다.
keys=['a','b','c','d']
z=dict.fromkeys(keys) # 이 경우 변수에 저장해야함.


print(z)


# 25.2 반복문으로 딕셔너리 키-값 쌍으로 모두 출력

x={'a':10,'b':20,'c':30,'d':40}
for i in x:
    print(i,end=' ') # 이경우 키만 출력 되므로....

# 이때 for in 뒤에 딕셔너리를 지정하고 items를 사용해야한다.
x={'a':10,'b':20,'c':30,'d':40}
print()
for key,value in x.items():
    print(key,value)

#25.3 딕셔너리 표현식

# {키:값 for 키,값 in 딕셔너리}
# dict({키:값 for 키, 값 in 딕셔너리})
# keys=['a','b','c','d']
# x1={key:value for key,value in dict.fromkeys(keys).items}
#

# 25.7 연습문제: 평균 점수 구하기

maria={'korean':94,'english':91,'mathmatics':89,'science':83}
average=sum(maria.values())/len(maria)
print(average)

#25.8 심사문제:

