#--------------------------------------
# 전역변수(Global Variable)와 지역변수(Local Variable)
#- 함수 내에서 전역 변수 값변경하고자 하는 경우는 추가 코드 필요
#- 추가 코드: global 전역 변수ㅕㅇ
#=> 주의 : 전역변수 값이 언제든지 함수로 변경이 될수 있는 상황
#         사용시에 주의 필요함
#------------------------------------------------------------
#- 지역변수(Local Variable)
# - 함수에 존재 하는 변수
# - 함수에서만 사용 가능한 변수
# - 함수가 종료 되면 변수들은 메모리에서 사라짐
#-------------------------------------------------------------
# 사용자 정의 함수 --------------------------------------------
def currentDate(year,month,day):
    #year,month,day => 지역변수
    print(f'Today:{year}/{month:0>2}/{day:0>2}')

def currentDate2(month,day):
    #month,day => 지역변수
    #year=> 전역변수
    #함수 내에서 전역변수의 값을 변경하고자 하는 경우, global 전역변수면

    print(f'Today :{year}/{month:0>2}/{day:0>2}')

def currentDate3(month,day,week):
    #month,day,week => 지역변수
    #year=> 전역변수
    global year
    year = year + 10
    print(f'Today :{year}/{month:0>2}/{day:0>2}/{week}요일')

#전역변수
year,month,day = 2024,1,8

# 함수 사용 즉 함수 호출------------------------------------------
currentDate3(month,day,"Friday")

#변수 값 확인 출력
print(f'year{year},month:{month},day:{day}')

#함수의 변수인 지역변수는 함수 밖에서 사용 불가
# print(f'week:{week}')
