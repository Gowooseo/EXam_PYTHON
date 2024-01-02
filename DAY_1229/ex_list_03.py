#--------------------------------------
# list의 원소/요소 데이터 변경 및 삭제
#--------------------------------------
# "Merry Christmas"의 문자 1개 1개를 원소로 가지는 리스트로 생성하기
msglist=list('Merry Christmas')

print(f'msglist={msglist}')

# => ' '데이터를 '***' 변경 -----------------------------------
print(f'msglist[5]=>{msglist[5]}')

msglist[5]='***'
print(f'msglist=>{msglist}')

#삭제 ==> del 데이터 또는 del(데이터)--------------------------------
del msglist[5]
print(f'msglist => {msglist}')



