#-------------------------------------------------
# 반복문 - 2 while 반복문
# - 반복의 횟수가 정해지지 않은 경우에 사용.
# - 반복의 횟수가 정해진 경우에도 사용가능/
#-------------------------------------------------
# [요청] 사용자로부터 좋아하는 음식명을 입력 받아 주세요.
#  => input()
#       단, 사용자가 '끝'이라는 음식명 입력 전까지 입력 받으세요.
#       => 몇번 입력 받아야 입력이 끝날지 알 수 없음.
#-------------------------------------------------

#-------------------------------------------------
# 반복문 - 2 while 반복문
# - 반복의 횟수가 정해지지 않은 경우에 사용.
# - 반복의 횟수가 정해진 경우에도 사용가능/
#-------------------------------------------------

# [요청] 사용자로부터 좋아하는 음식명을 입력 받아 주세요.
#  => input()
#       단, TOP 5로 가장 좋아 하는 음식 5개만 입력 받으세요.
#       => 사용자의 TOP5 음식명 출력
#-------------------------------------------------
# myFoods=[]
# for cnt in range(5):
#     food=input(f"{cnt+1}번째 좋아하는 음식명 입력 : ")
#     myFoods.append(food)
#
# #결과 출력 ==>
# print("당신은 ",end='')
# for food in myFoods:
#     print(food, end=', ' if myFoods[-1] != food else ' ')
# print("음식을 좋아하는 군요!")
TEST=False               #실습용 코드 제어 변수

if TEST:
    strFoods=""
    for cnt in range(5):
        food = input(f"{cnt + 1}번째 좋아하는 음식명 입력 : ")
        strFoods = strFoods + food
        strFoods = strFoods + food + (", " if cnt != 4 else ' ')
    #결과 출력==>
    print(f"당신은 {strFoods} 음식을 좋아하는 군요!")

#-------------------------------------------------
# 기본 while 문법
# while 조건식:
# <----> 실행코드
# <----> 실행코드
#-------------------------------------------------
# 타이머 프로그램 만들기 => 다운카운팅: 10 9 8 7 ....1
downCnt=10
while downCnt>=1:          #while downCnt>0:
    print(f'다운 카운팅 {downCnt}초')
    downCnt=downCnt-1
    downCnt-=1
#downCnt-=1(복합연산자 빼고 대입하세요)


#타이머 프로그램 만들기<===> 업카운팅:1,2,3,4 ,....10
upCnt=1
while upCnt<=10:
    print(f'업 카운팅 {upCnt}초')
    upCnt+=1    #upCnt=upCnt+1


# for 문으로 바꿔쓰기

# 다운카운팅(10~1 까지 이므로 range(10,0,-1))
for i in range(10,0,-1):
    print(f"다운카운팅 {i}초 ")

#업카운팅(1~10 까지 이므로 range(1,11))
for i in range(1,11):
    print(f"업카운팅 {i}초 ")
