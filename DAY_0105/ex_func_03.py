#------------------------------------------
# 다양한 함수의 형태-(1) 반환값 없는 함수
#------------------------------------------
#
#-  함수 생성 문법
#   def 함수이름(매개변수1,매개변수2,...,매개변수):
#   실행코드
#   실행코드
#-------------------------------------------
# 함수 기능 : 2개의 정수를 덧셈 후 출력해주는 기능
# 함수 이름: addTwo
# 매개변수: x,y
# 반환값: 없음
#----------------------------------------------------
def addTwo(x,y):
    value=x+y
    print(f'{x}+{y}={value}')


# 함수 사용 즉 함수 호출-------------------
addTwo(10,3)

#함수 호출 시에 매개변수 갯수와 데이터 동일하게 전달해야함!!'
#ERROR
#addTwo(10,10,10)
#addTwo(10)
#-------------------------------------------
# 함수 기능 : 영어 단어를 입력 받아서 모두 대문자로 변환 해주는 기능
# 함수 이름: convertCase
# 매개변수: word
# 반환값: 없음===> 아무일을 안함===> return 값이 필요함
#----------------------------------------------------
def convertCase(word):
    word=word.upper()
    return word


#함수 호출
#-------------------------------------------
# 함수 기능 : 시퀀스 객체의 모든 원소를 대문자로 변환 해주는 기능
# 함수 이름: convertCase2
# 매개변수: str 타입의 원소로 구성된 list
# 반환값: 없음
#----------------------------------------------------
def convertCase2(dataList):

    for idx in range(len(dataList)):
        dataList[idx]=dataList[idx].upper()

    # for idx,data in enumerate(dataList):
    #     dataList[idx]=data.upper()


datas=['Apple','banan','Mango']
# for data in datas:
#     print(data,data.upper())
for idx in range(len(datas)):
    datas[idx]=datas[idx].upper()

for idx,data in enumerate(datas):
    datas[idx]=data.upper()

print(datas)

#----------함수 사용 즉, 함수 호출
datas=['Apple','banan','Mango']

print(f'[BF] {datas}')

convertCase2(datas)

print(f'[AF]{datas}')
