#------------------------------------------
# 다양한 함수의 형태-(1) 기본
#------------------------------------------
# 함수 기능: 팩토리얼을 계산 후 계산 결과를 반환해주는 기능
#           팩토리얼이란? 3!
# 3!=3*2*1
# 함수 이름:factorial
# 매개 변수:x
# 반환값:계산 결과
def factorial(x):
    ret=1          #결과 저장 변수
    if x:
        for n in range(x, 0, -1):
            ret*=n
    return ret



# print(f'3! = {factorial(3)}')
# print(f'4! = {factorial(4)}')
# print(f'5! = {factorial(5)}')
# print(f'0! = {factorial(0)}')

#3!=3*2*1
#5!=5*4*3*2*1
#0!=1
#10!=10*9*8*7*6*5*4*3*2*1
#0!=1

# ret=1
# for n in range(5,0,-1):
#     ret*=n             #ret=ret*n
#     print(n,ret)

#------------------------------------------
# 함수 기능: 팩토리얼을 계산 후 계산 결과를 아래와 같은 형태로 반환해주는 기능
#           팩토리얼이란? 3!=3*2*1=6
# 3!=3*2*1
# 함수 이름:factorial2
# 매개 변수:n
# 반환값:계산 str

# ---------------------------------------------------------
def factorial2(x):
    strRet= f'{x}! : '
    intRet=1
    if x:
        for n in range(x,0,-1):
            intRet = intRet * n
            strRet=strRet+str(n)
            strRet = strRet +(' * ' if n !=1 else' = ')
            print(strRet,intRet)

    return strRet +str(intRet)



#--------------------------------------------------------------
# 함수 호출
print(factorial2(5))