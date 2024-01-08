#--------------------------------------------------------------------
#[실습] 2개의 정수를 입력 받은 후 4칙 연산 수행 결과를 반환하는 기능의
# 함수를 만들어 정의해 주세요.
#  함수이름: fourCalc
# 매개변수: n1,n2
# 반환결과 :사칙연산 결과
#--------------------------------------------------------------------
def fourCalc(n1,n2):
   return f'{n1}+{n2}={n1+n2},{n1}-{n2}={n1-n2},{n1}*{n2}={n1*n2},{n1}/{n2}={n1/n2}' if n2 else'0으로 나눌수 없음'

print(fourCalc(3,2))




#----------------------------------------------------------------------
#[실습2] 문자열을 16진수 코드값으로 변환하는 함수를 정의해주세요.
#         문자열---------> 코드값------------> 16진수 코드
#       함수명:getCode
#       매개변수:msg
#       반환결과: str
def getCode(message):
    ret=''
    for msg in message:
        ret+=hex(ord(msg))+'    '
    return ret

print(getCode('Good Luck'))