#----------------------------
#숫자5
#
#
#
# n=5
# while  n>0:
#     print(f'숫자{n}')
#     n=n-1

for i in range(5):
    print("입력해주세요.")

data=[1,2,3,4,5]
for i in data:
    print("입력해주세요.")
data1=1
while data1<=5:
    print("입력해주세요")
    data1+=1

# [요청] 사용자로부터 좋아하는 음식명을 입력 받아 주세요.
#  => input()
#       단, TOP 5로 가장 좋아 하는 음식 5개만 입력 받으세요.
#       => 사용자의 TOP5 음식명 출력
#-------------------------------------------------
# foods=[]
# for i in range(5):
#     food=input(f"{i+1}번째 좋아하는 음식을 입력하세요.")
#     foods.append(food)
# print(foods)

#. 사용자로부터 좋아하는 단어 3개를 입력받아, 저장 후 출력해주세요.
fwords=[]
for i in range(3):
    fword = input(f"{i + 1}번째 좋아하는 단어를 입력해주세요.:")
    fwords.append(fword)
print('당신은 ',end='')
for i in fwords:
    print(i,end=' ,' if fwords[-1]!=i else '')
print(' 음식을 좋아하는군요')
