#-------------------------------------------
# 팩킹(Packing) & 언팩킹(Unpacking)
#-------------------------------------------
msg="Happy New Year"

msgList=msg.split()
print(msgList[0],msgList[-1])

# 언팩킹(Unpacking) 방식
# 언팩킹 시 데이터 수와 변수의 수가 동일해야함!!!
m1, m2, m3=msg.split()
print(m1, m2, m3)
#데이터와 변수 수가 달라서 error 발생
#m1, m2=msg.split()
#print(m1, m2)

# 변수를 여러개 생성하는 경우
age=12
name="Hong"
job='학생'

# 튜플을 언팩킹하여서 생성 가능
age1,name1,job1=12,'Hong','학생'
info=(12,'Hong','학생')
info2=12,'Hong','학생'
