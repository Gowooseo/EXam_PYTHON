#[실습1] 알고 싶은 단을 입력 받고 해당 단을 출력해 주세요.
#-input()
#-특정 단의 구구단을 출력 => 반복문 사용하기.
#---------------------------------------------------------
# dan=input('단을 입력하십시오:')
# # if dan :
# #     #숫자로만 구성되어 있는지
# #     if dan.isdecimal():
# #         dan=int(dan)
# #         for num in range(1,10):
# #             print(f'{dan}*{num}={dan*num}')
# #     else:
# #         print('숫자만 입력 가능합니다.')
# # else:
# #     print("입력된 데이터가 없습니다.")
#
# if dan.isdecimal():
#     dan=int(dan)
#     for num in range(1,10):
#             print(f'{dan}*{num}={dan*num}')
# else:
#     print("정확한 데이터가 아닙니다.")
#
# # 거꾸로...
# if dan.isdecimal():
#     dan=int(dan)
#     for num in range(9,1,-1):
#             print(f'{dan}*{num}={dan*num}')
# else:
#     print("정확한 데이터가 아닙니다.")

# ----------------------------------------------
#[실습2] 2단 ~9단까지 모두 출력하세요.반복문 사용하기!!!
#-중첩 for 반복문
#-----------------------------------------------
# dan=2
# for num in range(1,10):
#     print(f'{dan}*{num}={dan * num}')
#
# dan=3
# for num in range(1,10):
#     print(f'{dan}*{num}={dan * num}')
# dan=4
# for num in range(1,10):
#     print(f'{dan}*{num}={dan * num}')
# dan=5
# for num in range(1,10):
#     print(f'{dan}*{num}={dan * num}')
# 단이 바뀌면 된다....
#
# for num in range(1,10):
#     for dan in range(2,10):
#         if num:
#             print(f'{num}*{dan}={num*dan}',end='  ')
#         else:
#             print(f'-----')






#
# for num in range(10):
#     for dan in range(2, 10):
#         if num:
#             print(f'{dan}*{num}={dan * num}', end='\n' if dan == 9 else '   ')
#         else:
#             print(f'----{dan}----', end='\n' if dan == 9 else '')



# 2 * 1 = 2  <== dan * num
for dan in range(2,10):
    for num in range(1,10):
        if num:
            print(f'{dan}*{num}={dan*num}',end='  ' if num!=9 else '\n')
        else:
            print(f'-----{dan}-------')


print("\n========================================\n")

for num in range(0, 10):
   for dan in range(2, 10):
       if num:
            print(f'{dan}*{num}={dan * num:2}',end='  ' if dan!=9 else '\n')
       else:
           print(f'{dan:-^6}',end='  ' if dan!=9 else '\n')