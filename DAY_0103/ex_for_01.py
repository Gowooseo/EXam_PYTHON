# 1~100사이에서 2의 배수에 해당하는 정수로 리스트 생성
result=list(range(2,101,2))
print(result)

# "2468101214182022...100"
# result=str(result)
# print(result)
# print(result[0],result[-6],result[-2],result[-1])

#int=> str 로 형변환
# result[0]=str(result[0])  # str(2) => '2'
# result[1]=str(result[2]

# 시퀀스 데이터 타입에서 원소/요소를 하나씩 뺴서 반복코드 수행 => for in 반복문
#---------------------------------------------------------------------
#'2468101214.....100'







strNum=''
for num in result:
    strNum=strNum+str(num)
print(f'type(strNUM)=> {type(strNum)},{strNum}')

#-----------------------------------------------------
# 리스트 안의 모든 원소를 str 타입으로 변환해서 저장하려면?
#-------------------------------------------------------
# 데이터의 인덱스 범위 => 0~ len(data)-1

print(f' before result => {result}')
for idx in range(len(result)):
    result[idx]=str(result[idx])
print(f'after result => {result}')


