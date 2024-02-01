#--------------------------------------------------
# # 문자열 여러개와 실수 숫자 여러개를 두 줄로 입력 받기=> input() 1개만 사용
# # - 첫번쨰 입력 받은 값을 Key로
# # - 두번재 입력 받은 값을 Value로
# # - 최종적으로 딕셔너리로 저장해주세요
#--------------------------------------------------
data=input("문자열과 실수 여러 개 입력(예:aa bb cc dd, 1.1 2.2 3.3 4.4):")

# 입력 형식이 맞을 경우만 딕셔너리에 저장
# -조건1)입력 "    , " 문자열 안에 ',' 존재해야 함=>
#--조건2) 문자열과 실수 갯수가 동일해야 함
if ',' in data:
    # dataList=data.split(',') #['aa bb cc', '1.1,2.2,3.3)
    # key=dataList[0].split()           # 'aa bb cc'
    # value=dataList[1].split()         # 1.1,2.2,3.3.split
    key,value=data.split()
    key=key.split()
    value=value.split()
    dataDict={}
    if len(key)==len(value):
        for num in range(len(key)):
            dataDict[key[num]]=float(value[num])

        dataDict2=dict(zip(key,value))
        print(f'dataDict: {dataDict}')
        print(f'dataDict2: {dataDict2}')
    else:
        print('정확한 형식이 아닙니다.')

else:
    print('정확한 형식이 아닙니다.')

# ----------------------------------------------
# 내장함수 zip()
#----------------------------------------------
x=[1,2,3,4,5]
y=[11,22,33,44,55]
z=[111,222,333,444,555]

result=zip(x,y,z)
print(f'result => {type(result)},{list(result)}')
