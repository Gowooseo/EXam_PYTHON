# 다양한 함수의 형태-특별한 함수(2)
#-매개변수의 갯수를 유동적으로 가변으로 하는 함수
# 키와 값의 덩어리 데이터
#- 형태: def 함수명(**data):
#- 가변 인자 함수
#- 매개변수 갯수: 0개~n개
#- 호출: 함수명(키1=값1)
#       함수명(키1=값1, 키2=값2, 키3= 값3) # 키값에 홋따옴표 쓰면 str타입이 되서 안됨.
#       함수명()
#------------------------------------------
#--------------------------------------------------
aDict={'name':'Hong','age':10}
aDict.update(job='학생')
aDict.update(job='학생',birth='1112',blood='A')
print(aDict)
aDict.update(점수1=100,점수2=200,점수3=300,점수4=400,점수5=500)
print(aDict)
#-------------------------------------------------------------------------
#함수 기능: 회원 가입 기능
#함수 이름: joinMember
#매개 변수: 이름,전화 번호,아이디,이메일,취미,주소,생일,......
#         가변 + 데이터 정보 함께
#         키워드파라미터 **member
#반환값 : '가입 완료 되었습니다.'
#----------------------------------------------------------------------------
def joinmember(**member):
    # print(type(member))
    #멤버 저장소에 멤버 추가하기
    # members.append(**member)
    members[f'M{len(members)+1}']=member

#----------------------------------------------------------------
# 함수 사용 즉 호출
#----------------------------------------------------------------
# 가입된 회원들 저장 변수
members={}
mList=[]
print(f'[BF] : {members}')

# 회원가입 기능 함수 호출
joinmember(name='Hong',age=17,birth='2020')
joinmember(id='Hong84',phone='010',job='actor',blood='B')
joinmember(id='baby', birth='2024',blood='A')

print(f'[AF] : {members}')

#-------------------------------------------------------------------------
#함수 기능: 회원 가입 기능
#함수 이름: joinMember
#매개 변수: 필수=>id,pw
#          선택=>  ** option 이름,전화 번호,아이디,이메일,취미,주소,생일,......
#         가변 + 데이터 정보 함께
#반환값 : '가입 완료 되었습니다.'
#----------------------------------------------------------------------------
def joinmember2(id,pw,**option): # 가변인자들은 앞에 못쓰고, 뒤쪽으로 보내버려야 한다(필수요소는 앞에 적기)
    # print(type(member))
    #멤버 저장소에 멤버 추가하기
    # members.append(**member)
    members[f'M{len(members)+1}']=option

#----------------------------------------------------------------
# 함수 사용 즉 호출
#----------------------------------------------------------------
# 가입된 회원들 저장 변수
members={}
print(f'[BF] : {members}')

# 회원가입 기능 함수 호출
joinmember2('h','ph',phone='010-2222-1212',blood='A')


print(f'[AF] : {members}')

#-------------------------------------------------------------------------
#함수 기능: 회원 가입 기능
#함수 이름: joinMember
#매개 변수: 필수=>id,pw
#          선택=>  ** option 이름,전화 번호,아이디,이메일,취미,주소,생일,......
#         가변 + 데이터 정보 함께
#반환값 : '가입 완료 되었습니다.'
#----------------------------------------------------------------------------
def joinmember3(id,pw,loc='외국인',gender='남자',**option): # 가변인자들은 앞에 못쓰고, 뒤쪽으로 보내버려야 한다(필수요소는 앞에 적기)
    # print(type(member))
    print(id,pw,loc,gender,option)

    #키=> id
    #값=>pw,loc='외국인',gender='남자',**option
    #           {'pw':'123','loc':'내국인;,'gender':'남자','etc':option}
    valueDict={}
    valueDict['pw']:pw
    valueDict['loc']: loc
    valueDict['gender']: gender
    valueDict['etc']: option
    members[id]=valueDict
    #---------------------------------------------
members={}
print(f'[BF] : {members}')

# 회원가입 기능 함수 호출
joinmember3('h','ph')
joinmember3('h','ph',gender='여자')
joinmember3('h','ph',phone='010-2222-1212',blood='A')


print(f'[AF] : {members}')
for m in members.items():
    print()

