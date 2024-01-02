'''1.아래에 데이터를 저장하는 코드를 작성하세요'''
#1-1)
KIM='kim1234@naver.com'
print(KIM[:7])
#1-2)
AD="http://www.naver.com"
print(AD[11:])
#1-3)
name='홍길동'
print(name[1:])
#1-4)
msg='AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRr'
print(msg[::2])
print(msg[1::2])
#1-5)
msg2='ABC1DEF2GHI3JKL4MNO5PQR6STU7VWX8YZ'
print(msg2[3::4])
#1-6)
phone='881120-1068234'
print(phone[0:6])
print(phone[7:])
print(phone.split('-'))
phones=phone.split('-')
print(phones[0])
print(phones[1])
#2.아래 조건에 맞게 코드 작성하세요
no1=int(input(f'정수 입력: '))
print(no1,hex(no1),oct(no1),bin(no1))
#3.아래 조건에 맞게 코드 작성하세요
# [조건]
# 3개의 단어를 입력 받은 후 가장 큰 단어, 가장 작은 단어를 출력 하세요. - input() 함수 3개 사용
# - 내장함수 max(), min() 사용
wo1=input('단어 1개 입력:')
wo2=input('단어 1개 입력:')
wo3=input('단어 1개 입력:')

print(f'코드 값이 가장 큰 단어:{max(wo1,wo2,wo3)}')
print(f'코드 값이 가장 작은 단어:{min(wo1,wo2,wo3)}')

#4. 아래 조건에 만족하도록 코드 작성하세요.
#[조건] - 본인이 원하는 메시지를 하나 정합니다. - input() 함수로 단어를 입력 받습니다. - 입력 받은 안어가 메시지 안에 존재하는지 여부를 출력하세요.
#[내가정한 메시지] “오늘은 행복한 목요일입니다.”
#[입력] 단어 입력 : 목요일
#[출력] ‘목요일’ 단어 메시지 존재 여부 : True
#[입력] 단어 입력 : happy
#[출력] ‘happy’ 단어 메지지 존재 여부 : False
shout='오늘은 행복한 목요일 입니다.'
thu=input('단어 입력: ')
print(f"'{thu}' 단어 메시지 존재 여부:{thu in shout}")

# 5. 아래 조건에 만족하도록 코드 작성하세요.
ddd='zoo'
print(f'{ddd} 코드값:' ,bin(ord(ddd[0])),bin(ord(ddd[1]))[2:],bin(ord(ddd[2]))[2:])


#(1) 문자 1개에 대한 코드값 => ort('문자 1개')
# (2) 원하는 진수 변환 => bin(10진수 코드값), hex(10진수 코드값)
print(f"'{ddd} 코드값: {bin(ord(ddd[0]))},{bin(ord(ddd[1]))[2:]},{bin(ord(ddd[2]))[2:]}")