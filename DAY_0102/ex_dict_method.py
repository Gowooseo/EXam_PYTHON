#--------------------------------
# dict 데이터 전용 함수 즉 메서드(Method)
#--------------------------------
# 빈 dict 타입  변수 생성----------------------------------
myDict={}

#데이터 추가=> myDict[키]=데이터
myDict['one']=100

# 데이터 추가 => update(키=데이터) 메서드
# 주의!!! zlsms str 타입만 가능, str 타입이지만 '',"" 사용 안됨
#myDict.update('two'=200)<=== ERROR
myDict.update(two=200)
myDict.update(two=200,_1=1000)
print(myDict)

#키만 추출해서 읽어오는 메서드 => keys() 메서드 -----------------------------
keys=myDict.keys()
print(f'myDict의 키들 :{keys}, {type(keys)}')

#값만 추출해서 읽어오는 메서드 => values() 메서드 -----------------------------
values=myDict.values()
print(f'myDict의 값들 :{values}, {type(values)}')

#키와 값을 추출해서 읽어오는 메서드 => items() 메서드 -----------------------------
# (키,값) 튜플 형식으로 묶어서
items=(myDict.items())
print(f'myDict의 키/값 묶음들 :{items}, {type(items)}')

# 원소/요소 단위 접근 위해서는 형변환이 필요함!!변수=list(변수items())
items=list(myDict.items())
print(f'myDict의 키/값 묶음들 :{items[0]}, {type(items[0])}')

# 원소/요소 모두 삭제해주는 메서드 => clear()메서드 ---------------
# myDict.clear()
# print(f'myDict :{myDict},{len(myDict)}')

# 원소/요소 데이터 읽기 메서드 => 변수명[키] ===> 값, get(키)메서드
# => 키가 존재하지 않으면 None 반환
print(f'myDict.get("one"):{myDict.get("one")},{myDict["one"]}')
print(f'myDict.get("three"):{myDict.get("three")}')

# 원소/요소 데이터 읽기 메서드 => 변수명[키] ===> 값, get(키)메서드
# => 키가 존재하지 않으면 기본값 반환
print(f'myDict.get("three",0):{myDict.get("three",0)}')
print(f'myDict.get("three","존재 하지 않음") :{myDict.get("three","존재 하지 않음")}')
#-----------------------------------------------------------
# 멤버 연산자 => 원소 in 여러개 저장 타입
#           => 원소 not in 여러개 저장 타입
# - 여러개 저장 타입:str,list,tuple,dict,set
#- dustks rufrhk => True/False
#-----------------------------------------------------------
aList=[1,2,3]
aTuple=11,22
aDict={1:100,2:100}
#                     => 데이터 즉 값 존재 여부
print(f'1 in aList: {1 in aList}')
print(f'1 in aTuple: {1 in aList}')
#                     => 키 존재 여부
print(f'1 in aDict: {1 in aList}')
print(f'1 in aDict: {100 in aList}')
# 딕셔너리 타입에서 in을 적용 할떄 key의 존재여부를 따른다 aDict의 키 중에 1이 있으므로 {1 in aList}
# 가 성립한다.=> True

#