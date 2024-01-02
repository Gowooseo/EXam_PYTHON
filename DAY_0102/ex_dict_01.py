#---------------------------------------------------
#[질문] 10명 학생에 대한 학점을 저장하기
# - 학생의 이름과 학점
# ---------------------------------------------------
# 방법1) 학생 이름 변수 10개 => stdName1 ~stdName10
#       학점 변수 10개      => jumsu1  ~ jumsu10
stdNum01='std01'
stdNum02='std02'
stdNum03='std03'
stdNum04='std04'
stdNum05='std05'
#  번거로움

# 방법2) 학생 이름 변수 10개 => stdName=[학생 이름1,....,학생 이름10]
#       학점 변수 10개      => stdJumsus=[점수1,...,점수10]
stdNums=['std01','std02','std03','std04','std05']
stdJumsus=[90,89,100,76,34]

# => 학번 03번 학생의 학번과 점수를 출력하세요~
idx=stdNums.index('std03')

print(f"{stdNums[idx]}학번 학생의 점수{stdJumsus[idx]}")

stdNumsJumsus=[['std01',90],['std02',89],['std03',100],['std04',76],['std05',34]]

#-------------------------------------------------------------
# dict 자료형
#- 연관되어 있는 데이터를 하나로 묶어서 저장하는 방식 => 연관배열
#- 형태=> 키: 데이터   (예: 주민번호:이름, 학번 : 전공 )
#- 조건 => 키가 중복되면 안됨!
#- 문법 => {키:데이터,키:데이터, .... 키:데이터N}
#-------------------------------------------------------------
stdNumsJumsu={'std01':90,'std02':89,'std03':100,'std04':76,'std05':34}
print(f'stdNumsJumsu:{len(stdNumsJumsu)}개,{type(stdNumsJumsus)},{stdNumsJumsus}')

#원소 읽는 방법 => 변수명[키]
print(f'stdNumsJumsu["std03"]=> {stdNumsJumsu["std03"]}')
#마지막 원소 지정하는 -1 사용=>-1에 대한 키가 없으면 ERROR
#print(f'stdNumsJumsu[-1]=>{stdNumsJumsu[-1]}')

#-------------------------------------------------------
#원소/요소 추가방법 => 변수명[새로운 키]= 데이터
#-------------------------------------------------------
# 학번 10인 학생의 점수 99.8 저장 즉 추가하기
stdNumsJumsu['std10']=99.8
print(f'stdNumsJumsu:{len(stdNumsJumsu)}개,{stdNumsJumsus}')

#-------------------------------------------------------
#원소/요소 추가방법 => 변수명[새로운 키]= 데이터
#-------------------------------------------------------
# 학번 10인 학생의 점수 99점으로 변경
stdNumsJumsu['std10']=99
print(f'stdNumsJumsu:{len(stdNumsJumsu)}개,{stdNumsJumsus}')

#-----------------------------
# 원소/요소 데이터 삭제 => del 변수명[키] 또는 del(변수명[키])
#----------------------------------------------------------
del stdNumsJumsu['std02']
print(f'stdNumsJumsu:{len(stdNumsJumsu)}개,{stdNumsJumsus}')

del stdNumsJumsu['std10']
print(f'stdNumsJumsu:{len(stdNumsJumsu)}개,{stdNumsJumsus}')

del stdNumsJumsu['std01']
print(f'stdNumsJumsu:{len(stdNumsJumsu)}개,{stdNumsJumsus}')