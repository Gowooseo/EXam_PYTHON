#----------------------------
#[실습1] 2개 숫자  데이터 입력 받은 후 2개의 값을 산술 연산 결과를 출력해주세요.
num1=int(input('숫자 1개 입력:'))
num2=int(input('숫자 1개 입력:'))
print(f'{num1}+{num2}={num1+num2}')
print(f'{num1}-{num2}={num1-num2}')
print(f'{num1}*{num2}={num1*num2}')
print(f'{num1}/{num2}={num1/num2}')
print(f'{num1}%{num2}={num1%num2}')
print(f'{num1}//{num2}={num1//num2}')
print(f'{num1}**{num2}={num1**num2}')
#----------------------------
#[실습2][실습1]에서 입력 받은 숫자 데이터를 활용하여 비교 연산 결과를 출력하세요.
#>,<,>=,<===,!=
#     [출력 예시] 10>4   => True
                 #10==4=> False
print(f'{num1}>{num2} => {num1>num2}')
print(f'{num1}<{num2} => {num1<num2}')
print(f'{num1}>={num2} => {num1>=num2}')
print(f'{num1}<={num2} => {num1<=num2}')
print(f'{num1}!={num2} => {num1!=num2}')
#--------------------------------------
#----------------------
# [실습3][실습1]에서 입력 받은 숫자 데이터를 활용하여
# 최댓값과 m2값을 추가로 입력 받은 후 논리 연산 결과 출력하세요.
# [출력 예시] 10>4 and 10>m1값  => True
#                  10>4 and 10>최솟값=> True
#                  not 10   => False
#

m1=int(input('최댓값을 입력해주세요:'))
m2=int(input('최솟값을 입력해주세요:'))
print(f'{num1} > {num2} and {num1} > {m1}=> {num1 > num2 and num1 > m1}')
print(f'{num1} < {num2} and {num1} < {m2}=> {num1 < num2 and num1 < m2}')


# not 연산자=> not 데이터, not 변수명

print(f'not {num1} => {not num1}')