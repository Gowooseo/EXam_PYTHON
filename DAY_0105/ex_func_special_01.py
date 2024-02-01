# 다양한 함수의 형태-특별한 함수(1)
#-매개변수의 갯수를 유동적으로 가변으로 하는 함수
#- 형태: def 함수명( *data):
#- 가변 인자 함수
#- 매개변수 갯수: 0개~n개
#------------------------------------------
# 2개 정수를 덧셈 후 결과를 반환 하는 함수 생성-----------------
def plus(x,y):
    return x+y

# 5개 정수를 덧셈 후 결과를 반환 하는 함수 생성-----------------
def plus5(x,y,z,w,q):
    return x+y+z+w+q

# 3개 정수를 덧셈 후 결과를 반환 하는 함수 생성-----------------
def plus3(a,b,c):
    return a+b+c

#----------------------한도 끝도 없다.....# 받는 값의 개수가 변화하면 좋을텐데....



# ---------------------------------------
# 함수 기능: 전달 받은 숫자를 모두 덧셈한 결과 반환 기능
#- 형태: addNumber
#- 매개변수 갯수: *nums
# 반환값: 계산 결과
#-------------------------
def addNumber(*data):
    print(type(data))
    ret=0
    for d in data:
        ret=ret+d
    return ret
# 함수 사용 즉 함수 호출-----------------------------------------------
print(addNumber(1,2,3))
print(addNumber(10))
print(addNumber())

# *시퀀스/반복이 가능한 객체 => 내부에 모든 원소를 하나씩 풀어서 전달: 언팩킹
print(addNumber(*range(1,11)))

a=[11,22,33,44]
aTuple='a','b','c'
aDict={'jj':'Hong','age':100}

print(a,aTuple,aDict)
print(*aDict,sep='-')


print()
print(10)
print(10,30,40)

