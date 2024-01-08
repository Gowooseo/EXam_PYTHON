#----------------------------------------------
# 참조형 변수=> 데이터의 주소 저장
# ----------------------------------------------

num1=[]
print(f'num=> {id(num)},{type(num)}')

num2=[11,22.1]
print(f'num2=> {id(num)},{type(num)}')
print(f'num2[0]=>{id(num[0])},{type(num[0])} ')
print(f'num2[1]=> {id(num[1])},{type(num[1])}')

print("============== 값 변경 =================")
# 리스트의 원소를 변경하는 경우

num2[0]=100
print(f'num2=>{id(num2)},{type(num2)} ')
print(f'num2[0]=> {id(num2[0])},{type(num2[0])}')

num2=num1
print(f'num1=> {id(num1)},{num1}')
print(f'num2=> {id(num2)},{num2}')

num1[0]=77
print(f'num1=> {id(num1)},{num1}')
print(f'num2=> {id(num2)},{num2}')

