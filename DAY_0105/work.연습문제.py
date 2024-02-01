# 1.문자열 리스트를 입력 받아서 내림차순 결과 가장 낮은 문자열과 가장 높은 문자열을
# 출력하는 함수를 구현하세요.






#2. . 키보드로 입력 받은 데이터 중에서 숫자만 모두 저장하여 합계, 최대값, 최소값을
 # 출력하는 함수를 구현하세요.
# data=input('데이터 입력:')
#  def sum1(*a):
#     print(sum(*a))
#  def max1(*a):
#     print(max(*a))
# def min1(*a):
#     print(min(*a))


#3. 아래 조건을 만족하는 코드를 작성 하세요.
# - ‘q’, ‘Q’ 입력 전까지 동작
# - 대문자 Q 제외한 나머지 알파벳 입력 시 ♠ 출력
# - 소문자 q 제외한 나머지 알파벳 입력 시 ♤ 출력
# - 0 ~ 9 숫자 입력 시 숫자만큼의 ◎ 출력






#4.아래 조건을 만족하는 코드를 구하세요

# - 수의 범위 : 1 ~ 100
# - 3의 배수 숫자 - 7의 배수 숫자
# - 8의 배수 숫자
# - 3, 7, 8의 배수 숫자로 구성된 숫자만 출력
# # - 단!! 중복된 숫자는 제거 하세요
#
# for i in range(1,101):
#     if i/3==0 or i/7==0 or i/8==0:
#         print(i)
#         if


#5.문자열을 입력하면 코드값을 아래와 같이 출력해주는 함수를 입력해주세요.
# [입 력]
# data =“가나다”
# [함수호출]
# [출 력]
# "가나다"
# 의
# 인코딩: 0xac000
# xb0980xb2e4
# "가나다의 인코딩"
# : 0b10101100000000000
# "가나다의 인코딩":b10110000100110000b1011001011100100
# def datatransmision():
#     data=input('문자를 입력하세요')
#     for i in data:
#


#6.문자열 리스트와 정수 1개를 입력하면 아래와 같이 출력하는 함수를 구현해주세요.




#7.아래와 같이 출력되는 함수를 구하세요.

# def printint():
#     nums=input("정수 리스트를 입력(예:[1,2,3,4,5,6])")
#
#18.

# 19.
num=input('팩토리얼 수 입력:')
def factorial(x):
    if x==1:
        return 1
    return x*factorial(x-1)

while True:

print(f'{num}!=>{factorial(int(num))}')



#26.아래 출력결과가 나오도록 코드를 작성하세요
height=int(input())

#문제 만들기
for i in range(1,height+1):
    sss=2*i-1
    if height<=6:
        print(' '*(height-i)+ "*"*sss,sep=' ')
    elif 6<height and height<=11:
        print(' '*sss+"*"*(height-i),sep=' ')
    else:
        print("Good luck 2023")
        break

