#--------------------------------------------------#
# 메서드 => 특정 데이터 타입의 전용 함수를 메서드(Method)라고 부름
# - 범용의 함수와 식별하기 위해서 지정한 호칭
# - 사용법: 데이터.메서드명() 또는 변수명.메서드명()
#----------------------------------
# List 전용 메서드 살펴보기 ===================================
# [1] 리스트에 데이터 추가해주는 메서드
nums=[]
print(f'nums :{len(nums)}개, {nums}')
nums.append(10)
nums.append('One')
nums.append(True)
print(f'nums :{len(nums)}개, {nums}')

#[1]리스트에 데이터 추가 해주는 메서드 => insert(위치 인덱스,데이터) 지정 위치에 추가
nums.insert(0,2024)
print(f'nums: {len(nums)}개, {nums}')

nums.insert(-1,["ABC","DEF"])
print(f'nums: {len(nums)}개, {nums}') # 원래 있던 TRUE는 옆으로 밀린다.

# 'DEF'만 삭제
del nums[-2][-1]
print(f'nums: {len(nums)}개, {nums}')

# 리스트 안에 모든 원소 삭제 해서 빈 리스트 만들어 주세요!
del nums[:]
print(f'nums: {len(nums)}개, {nums}')

# 리스트 안에 원소/요소 정렬해주는 메서드 => sort() 오름차순 정렬
#- 오름차순 : 작은 데이터 >>> 큰 데이터
nums.append(98)
nums.append(91)
nums.append(92)
nums.append(93)
nums.append(94)

nums.sort()
print(f'nums: {len(nums)}개, {nums}')

#nums=nums.sort()
#print(f'nums:{len(nums)}개,{nums}') 저장을 해버리면 none타입이므로 원본이 바뀌는 거라서 오류가 뜸

# 내림차순: 큰 데이터 >> 작은 데이터 순서로
nums.sort(reverse=True) #역순 매개변수 값을 True 설정
print(f'nums: {len(nums)}개, {nums}')

#[3] 리스트 안에 원소/요소의 현재 위치를 반대로 뒤집어 주는 메서드 => sort() 오름차순 정렬
# 원소/요소 데이터 값은 비교 x, 순서만 변경 함
nums.reverse()
print(f'nums: {len(nums)}개, {nums}')

#[4] 리스트 안에 원소/요소를 삭제해주는 메서드 => remove(데이터)
#-리스트에서 지정된 '값'의 원소 삭제
#- 없는 값/데이터 삭제 요청 시 Error 발생시킴!!
#nums.remove(0)
#print(f'nums: {len(nums)}개, {nums}')

#nums.remove(0)
#print(f'nums: {len(nums)}개, {nums}')
#[5] 리스트 안에 모든 원소/요소를 삭제하는 메서드 -> clear()
nums.clear()
print(f'nums: {len(nums)}개, {nums}')

# insert,pop등은 위치를 지정해서 넣거나 끄집어 낸다.
#[5] 리스트 안에 원소/요소를 꺼내는 메서드 -> pop()
nums.append(10)
nums.append(-3)
nums.append(7)

#제일 마지막 원소/요소 데이터 꺼내기 => pop()
nums.pop()
print(f'nums: {len(nums)}개, {nums}')

# 특정 위치에 원소/요소 데이터 꺼내기 => pop(인덱스)
nums.pop(0)
print(f'nums: {len(nums)}개, {nums}')
# del과 pop의 차이점, pop은 꺼내온 값을 보여주므로, 꺼낸 값을 저장할 필요가 있다.

#[7] 리스트에서 특정 원소/요소 데이터가 몇개 존재하는지 카운팅해주는 메서드 -> count(데이터)
print(nums.count('A'))
print(nums.count(-3))

# [8] 리스트를 확장시키는 메서드 => extend(여러 개의 데이터 저장한 데이터 타입)
nums.extend([11,22,33])
print(f'nums: {len(nums)}개, {nums}')

nums.extend([])
print(f'nums: {len(nums)}개, {nums}')
# 문자로 할 경우 1칸당 1개씩....
nums.extend("새해 복 많이 받으세요")
print(f'nums: {len(nums)}개, {nums}')

nums.extend(["새해 복 많이 받으세요"])
print(f'nums: {len(nums)}개, {nums}')
# 정수 개체는 시퀀스 개체(list,str,range등등)가 아니므로 순서가 없음, 따라서 반복할 수 없다는 오류가 등장함.
# nums.extend(2024)   # 시퀀스 또는 반복가능한 데이터만 가능
# print(f'nums: {len(nums)}개, {nums}')

#[9] 리스트를 복사해주는 메서드 => 얕은 복사 copy(),복사본이 나오므로 새 변수로 따로 저장.
nums.append([100,200])
nums2=nums.copy()

print(f'nums: {len(nums)}개, {nums}')
print(f'nums2: {len(nums2)}개, {nums2}')

#nums의 -1번 요소의 데이터를 2024로 변경
nums[-2]=2024
print(f'nums: {len(nums)}개, {nums}')
print(f'nums2: {len(nums2)}개, {nums2}')

#nums의 -1번 요소의 0번 요소의 데이터를 77로 변경
#nums만 바꾸려고 했는데 nums2도 바뀌어 있다.....
#list는 원소의 주소를 저장하는데 그 원소를 바꾸게 되면 그것이 같이 저장된다(얕은 복사)
nums[-1][0]=77
print(f'nums: {len(nums)}개, {nums}')
print(f'nums2: {len(nums2)}개, {nums2}')

