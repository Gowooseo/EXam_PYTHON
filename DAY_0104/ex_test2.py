#--------------------------------------------------------
# [실습1] 아래 데이터에 있는 원소를 화면에 한줄에 한개씩 출력
#--------------------------------------------------------
datas=['Apple', 'Banana', 'Orange', 'Kiwi', 'Grape']

for i in datas:
    print(i)

idx=0
while idx<5:
    print(datas[idx])
    idx=idx+1

#--------------------------------------------------------
# [실습2] 아래 데이터에 있는 원소를 화면에 한줄에 한개씩 출력
#--------------------------------------------------------
jumsus=[98, 45, 100, 45, 98, 70, 34, 99, 100]

for d in jumsus:
    print(d)

idx1=0
while idx1<9:
    print(jumsus[idx1])
    idx1=idx1+1


#--------------------------------------------------------
# [실습3] 키보드로 입력 받은 데이터를 저장합니다.
#        좋아하는 숫자를 10개 입력 받습니다.
#        단, input() 함수를 10번 사용해 주세요.
#--------------------------------------------------------
num=[]
for i in range(10):
   nums =input(f'좋아하는 {i+1}번째 숫자를 입력해주세요.: ')
   num.append(nums)
print(num)

num2=[]
i=1
while i<=10:
    nums = input(f'좋아하는 {i}번째 숫자를 입력해주세요.: ')
    num2.append(nums)
    i=i+1
print(num2)